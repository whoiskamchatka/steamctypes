"""Deliver Steam callbacks and asynchronous call results."""

import contextlib
import ctypes
import functools
import threading
import time
import warnings
from collections.abc import Callable
from typing import Any, Generic, TypeVar, cast

from steamctypes._generated import SDK_VERSION
from steamctypes._generated.callbacks import CALLBACKS
from steamctypes._generated.constants import k_uAPICallInvalid
from steamctypes._generated.enums import ESteamAPICallFailure
from steamctypes._generated.functions import ACCESSORS
from steamctypes._generated.structs import CallbackMsg_t, SteamAPICallCompleted_t
from steamctypes._native import Native
from steamctypes.errors import CallResultError, SteamError, SteamWarning

T = TypeVar("T", bound=ctypes.Structure)
Handler = Callable[[Any], object]
DoneCallback = Callable[[], object]

# The session is user-side, so an id shared with a game server struct delivers the user struct,
# and only that struct can be subscribed to.
_STRUCTS = {callback_id: structs[0] for callback_id, structs in CALLBACKS.items()}
_IDS = {struct: callback_id for callback_id, struct in _STRUCTS.items()}
_COMPLETED_ID = _IDS[SteamAPICallCompleted_t]
_WAIT_INTERVAL = 0.01  # seconds between attempts to pump a frame in CallResult.wait()
# Warnings point at the code that called Steam.run_callbacks() or CallResult.wait(): both reach
# _read() through the same number of frames.
_READ_STACKLEVEL = 6


def callback_id_of(struct: type[ctypes.Structure]) -> int:
    try:
        return _IDS[struct]
    except KeyError:
        raise TypeError(f"{struct.__name__} is not a Steam callback struct") from None


class _Pending(Generic[T]):
    """The state a CallResult shares with the dispatcher that completes it."""

    def __init__(self, struct: type[T]) -> None:
        self.struct = struct
        self.lock = threading.Lock()
        self.finished = threading.Event()
        self.value: T | None = None
        self.error: SteamError | None = None
        self.callbacks: list[DoneCallback] = []

    def finish(self, value: T | None, error: SteamError | None) -> list[DoneCallback]:
        """Record the outcome, then mark it done; return the done callbacks to run."""
        with self.lock:
            self.value, self.error = value, error
            self.finished.set()
            callbacks, self.callbacks = self.callbacks, []
        return callbacks


class CallResult(Generic[T]):
    """The result of an asynchronous Steam API call, delivered by Steam.run_callbacks()."""

    def __init__(self, pending: _Pending[T], dispatcher: "Dispatcher") -> None:
        self._pending = pending
        self._dispatcher = dispatcher

    def done(self) -> bool:
        return self._pending.finished.is_set()

    def result(self) -> T:
        """The result struct. Raises if the call failed or has not completed yet."""
        pending = self._pending
        if not pending.finished.is_set():
            raise SteamError("the call has not completed yet")
        if pending.error is not None:
            raise pending.error
        assert pending.value is not None
        return pending.value

    def add_done_callback(self, fn: "Callable[[CallResult[T]], object]") -> None:
        """Call fn(self) when the call completes, or now if it already has."""
        with self._pending.lock:
            if not self._pending.finished.is_set():
                self._pending.callbacks.append(functools.partial(fn, self))
                return
        fn(self)

    def wait(self, timeout: float | None = None) -> T:
        """Pump frames until done, return result(); handler errors raise as in run_callbacks()."""
        dispatcher, finished = self._dispatcher, self._pending.finished
        if dispatcher.in_handler():
            raise SteamError("CallResult.wait() cannot run inside a callback handler")
        deadline = None if timeout is None else time.monotonic() + timeout
        while not finished.is_set():
            remaining = None if deadline is None else deadline - time.monotonic()
            if remaining is not None and remaining <= 0:
                raise TimeoutError("the Steam API call did not complete in time")
            # Pump a frame unless another thread is running one; either way, give the
            # completion a moment to arrive before trying again.
            dispatcher.try_run()
            finished.wait(_WAIT_INTERVAL if remaining is None else min(_WAIT_INTERVAL, remaining))
        return self.result()


class Dispatcher:
    """Drains the manual dispatch queue of one pipe and delivers what it finds."""

    def __init__(self, native: Native, pipe: int) -> None:
        self.native = native
        self._pipe = pipe
        self._subscribers: dict[type[ctypes.Structure], list[Handler]] = {}
        self._pending: dict[int, _Pending[Any]] = {}
        self._warned_ids: set[int] = set()
        self._warned_results: set[type[ctypes.Structure]] = set()
        # Held while a frame drains the queue and while a call registers its handle, so no frame
        # can consume a completion whose handle is not registered yet. Subscriptions and close()
        # take it too, so nothing is added after close() clears it.
        self._frame = threading.Lock()
        self._runner: int | None = None  # the thread running a frame
        self._closed = False

    def subscribe(self, struct: type[ctypes.Structure], handler: Handler) -> None:
        callback_id_of(struct)
        with self._frame_lock():
            if self._closed:
                raise SteamError("Steam has been shut down")
            self._subscribers.setdefault(struct, []).append(handler)

    def unsubscribe(self, struct: type[ctypes.Structure], handler: Handler) -> None:
        handlers = self._subscribers.get(struct, [])
        if handler not in handlers:
            raise ValueError(f"{handler!r} is not subscribed to {struct.__name__}")
        handlers.remove(handler)

    def async_call(self, function: str, struct: type[T], *args: object) -> CallResult[T]:
        """Make a flat API call that returns a SteamAPICall_t and track its result in struct."""
        callback_id_of(struct)
        with self._frame_lock():
            if self._closed:
                raise SteamError("Steam has been shut down")
            handle = self.native[function](*args)
            pending = _Pending(struct)
            if handle == k_uAPICallInvalid:
                invalid = ESteamAPICallFailure.k_ESteamAPICallFailureInvalidHandle
                pending.finish(None, CallResultError(invalid))
            else:
                self._pending[handle] = pending
        return CallResult(pending, self)

    def in_handler(self) -> bool:
        return self._runner == threading.get_ident()

    def run(self) -> int:
        """Dispatch one frame, after any frame running on another thread.

        Returns how many callbacks reached a subscriber or call result.
        """
        if self.in_handler():
            raise SteamError("run_callbacks() cannot run inside a callback handler")
        with self._frame:
            dispatched = self._locked_frame()
        if dispatched is None:
            raise SteamError("Steam has been shut down")
        return dispatched

    def try_run(self) -> int | None:
        """Dispatch one frame, or return None if a frame is running or Steam was shut down."""
        if not self._frame.acquire(blocking=False):
            return None
        try:
            return self._locked_frame()
        finally:
            self._frame.release()

    def close(self) -> list[DoneCallback]:
        """Fail pending call results and drop subscriptions; return the done callbacks to run.

        Waits for a frame or call registration running on another thread.
        """
        with self._frame:
            self._closed = True
            pending, self._pending = self._pending, {}
            self._subscribers.clear()
            return [
                callback
                for call in pending.values()
                for callback in call.finish(
                    None, SteamError("Steam was shut down before the call completed")
                )
            ]

    def _frame_lock(self) -> contextlib.AbstractContextManager[object]:
        """The frame lock, or nothing if this thread's frame already holds it."""
        return contextlib.nullcontext() if self.in_handler() else self._frame

    def _locked_frame(self) -> int | None:
        if self._closed:
            return None
        self._runner = threading.get_ident()
        try:
            return self._run_frame()
        finally:
            self._runner = None

    def _run_frame(self) -> int:
        native, pipe = self.native, self._pipe
        native["SteamAPI_ManualDispatch_RunFrame"](pipe)
        message = CallbackMsg_t()
        dispatched = 0
        errors: list[Exception] = []
        while native["SteamAPI_ManualDispatch_GetNextCallback"](pipe, message):
            # Handlers run before the free: pointer fields point into the message, which
            # FreeLastCallback releases.
            try:
                reached, deliveries = self._read(message)
                dispatched += reached
                for deliver in deliveries:
                    try:
                        deliver()
                    except Exception as error:
                        errors.append(error)
            finally:
                native["SteamAPI_ManualDispatch_FreeLastCallback"](pipe)
        if errors:
            raise ExceptionGroup("callback handlers raised exceptions", errors)
        return dispatched

    def _read(self, message: CallbackMsg_t) -> tuple[bool, list[DoneCallback]]:
        """Copy the message's payload.

        Returns whether it reached a subscriber or a pending call result, and the calls that
        deliver it.
        """
        callback_id, size = message.m_iCallback, message.m_cubParam
        struct = _STRUCTS.get(callback_id)
        if struct is None:
            return False, []
        if size != ctypes.sizeof(struct):
            if callback_id not in self._warned_ids:
                self._warned_ids.add(callback_id)
                warnings.warn(
                    f"skipping callback {callback_id} ({struct.__name__}): Steam sent {size} "
                    f"bytes, steamctypes expects {ctypes.sizeof(struct)}. The steam_api library "
                    f"may not be from Steamworks SDK {SDK_VERSION}.",
                    SteamWarning,
                    stacklevel=_READ_STACKLEVEL,
                )
            return False, []
        handlers = tuple(self._subscribers.get(struct, ()))
        completes_call = callback_id == _COMPLETED_ID
        if not handlers and not completes_call:
            return False, []
        data = struct.from_buffer_copy(ctypes.string_at(message.m_pubParam, size))
        deliveries: list[DoneCallback] = [functools.partial(h, data) for h in handlers]
        pending = self._pending.pop(data.m_hAsyncCall, None) if completes_call else None
        if pending is not None:
            deliveries += self._complete(cast(SteamAPICallCompleted_t, data), pending)
        return bool(handlers) or pending is not None, deliveries

    def _complete(
        self, completed: SteamAPICallCompleted_t, pending: _Pending[Any]
    ) -> list[DoneCallback]:
        """Fetch the result of a completed call and settle it; return its done callbacks."""
        handle, struct = completed.m_hAsyncCall, pending.struct
        expected = (callback_id_of(struct), ctypes.sizeof(struct))
        if (completed.m_iCallback, completed.m_cubParam) != expected:
            message = (
                f"{struct.__name__}: Steam reports call result {completed.m_iCallback} of "
                f"{completed.m_cubParam} bytes, steamctypes expects {expected[0]} of {expected[1]} "
                f"bytes. The steam_api library likely comes from another SDK version than "
                f"{SDK_VERSION}."
            )
            if struct not in self._warned_results:
                self._warned_results.add(struct)
                warnings.warn(message, SteamWarning, stacklevel=_READ_STACKLEVEL + 1)
            mismatched = ESteamAPICallFailure.k_ESteamAPICallFailureMismatchedCallback
            return pending.finish(None, CallResultError(mismatched, message))
        result = struct()
        failed = ctypes.c_bool()
        fetched = self.native["SteamAPI_ManualDispatch_GetAPICallResult"](
            self._pipe, handle, ctypes.addressof(result), expected[1], expected[0], failed
        )
        if fetched and not failed.value:
            return pending.finish(result, None)
        utils = self.native[ACCESSORS["ISteamUtils"]["user"]]()
        reason = self.native["SteamAPI_ISteamUtils_GetAPICallFailureReason"](utils, handle)
        return pending.finish(None, CallResultError(reason))
