"""Deliver Steam callbacks and asynchronous call results."""

import ctypes
import functools
import threading
import time
import warnings
from collections.abc import Callable
from typing import Any, Generic, TypeVar

from steamctypes._generated import SDK_VERSION
from steamctypes._generated.callbacks import CALLBACKS
from steamctypes._generated.enums import ESteamAPICallFailure
from steamctypes._generated.functions import ACCESSORS
from steamctypes._generated.structs import SteamAPICallCompleted_t
from steamctypes._native import CallbackMsg_t, Native
from steamctypes.errors import CallResultError, SteamError, SteamWarning

T = TypeVar("T", bound=ctypes.Structure)
Handler = Callable[[Any], object]

# The session is user-side, so an id shared with a game server struct reads the user struct.
_STRUCTS = {callback_id: structs[0] for callback_id, structs in CALLBACKS.items()}
_IDS = {struct: callback_id for callback_id, structs in CALLBACKS.items() for struct in structs}
_COMPLETED_ID = _IDS[SteamAPICallCompleted_t]
_WAIT_INTERVAL = 0.01  # seconds between frames in CallResult.wait()


def _id_of(struct: type[ctypes.Structure]) -> int:
    try:
        return _IDS[struct]
    except KeyError:
        raise TypeError(f"{struct.__name__} is not a Steam callback struct") from None


class _Pending(Generic[T]):
    """The state a CallResult shares with the dispatcher that completes it."""

    def __init__(self, struct: type[T]) -> None:
        self.struct = struct
        self.lock = threading.Lock()
        self.done = False
        self.value: T | None = None
        self.error: SteamError | None = None
        self.callbacks: list[Callable[[], object]] = []

    def finish(self, value: T | None, error: SteamError | None) -> list[Callable[[], object]]:
        """Record the outcome and return the done callbacks to run."""
        with self.lock:
            self.done, self.value, self.error = True, value, error
            callbacks, self.callbacks = self.callbacks, []
        return callbacks


class CallResult(Generic[T]):
    """The result of an asynchronous Steam API call, delivered by Steam.run_callbacks()."""

    def __init__(self, pending: _Pending[T], run_callbacks: Callable[[], object]) -> None:
        self._pending = pending
        self._run_callbacks = run_callbacks

    def done(self) -> bool:
        return self._pending.done

    def result(self) -> T:
        """The result struct. Raises if the call failed or has not completed yet."""
        pending = self._pending
        if not pending.done:
            raise SteamError("the call has not completed yet")
        if pending.error is not None:
            raise pending.error
        assert pending.value is not None
        return pending.value

    def add_done_callback(self, fn: "Callable[[CallResult[T]], object]") -> None:
        """Call fn(self) when the call completes, or now if it already has."""
        with self._pending.lock:
            if not self._pending.done:
                self._pending.callbacks.append(functools.partial(fn, self))
                return
        fn(self)

    def wait(self, timeout: float | None = None) -> T:
        """Run callbacks until the call completes, then return result(). TimeoutError if slower."""
        deadline = None if timeout is None else time.monotonic() + timeout
        while not self.done():
            if deadline is not None and time.monotonic() >= deadline:
                raise TimeoutError("the Steam API call did not complete in time")
            self._run_callbacks()
            if not self.done():
                time.sleep(_WAIT_INTERVAL)
        return self.result()


class Dispatcher:
    """Drains the manual dispatch queue of one pipe and delivers what it finds."""

    def __init__(self, native: Native, pipe: int) -> None:
        self.native = native
        self._pipe = pipe
        self._subscribers: dict[type[ctypes.Structure], list[Handler]] = {}
        self._pending: dict[int, _Pending[Any]] = {}
        self._warned: set[int] = set()
        self._running = threading.Lock()
        self._runner: int | None = None
        self._closed = False

    def subscribe(self, struct: type[ctypes.Structure], handler: Handler) -> None:
        _id_of(struct)
        if self._closed:
            raise SteamError("Steam has been shut down")
        self._subscribers.setdefault(struct, []).append(handler)

    def unsubscribe(self, struct: type[ctypes.Structure], handler: Handler) -> None:
        handlers = self._subscribers.get(struct, [])
        if handler not in handlers:
            raise ValueError(f"{handler!r} is not subscribed to {struct.__name__}")
        handlers.remove(handler)

    def call_result(self, handle: int, struct: type[T]) -> CallResult[T]:
        _id_of(struct)
        if self._closed:
            raise SteamError("Steam has been shut down")
        pending = _Pending(struct)
        if handle == 0:  # k_uAPICallInvalid
            pending.finish(
                None, CallResultError(ESteamAPICallFailure.k_ESteamAPICallFailureInvalidHandle)
            )
        else:
            self._pending[handle] = pending
        return CallResult(pending, self.run)

    def in_handler(self) -> bool:
        return self._runner == threading.get_ident()

    def run(self) -> int:
        """Dispatch one frame and return how many callbacks reached a subscriber or call result."""
        if not self._running.acquire(blocking=False):
            raise SteamError("run_callbacks() is already running")
        self._runner = threading.get_ident()
        try:
            if self._closed:
                raise SteamError("Steam has been shut down")
            return self._run_frame()
        finally:
            self._runner = None
            self._running.release()

    def close(self) -> None:
        """Fail pending call results and drop subscriptions. Waits for a running dispatch."""
        with self._running:
            self._closed = True
            pending, self._pending = self._pending, {}
            self._subscribers.clear()
        # Done callbacks only run inside run_callbacks(), which can no longer happen.
        for call in pending.values():
            call.finish(None, SteamError("Steam was shut down before the call completed"))

    def _run_frame(self) -> int:
        native, pipe = self.native, self._pipe
        native["SteamAPI_ManualDispatch_RunFrame"](pipe)
        message = CallbackMsg_t()
        dispatched = 0
        errors: list[Exception] = []
        while native["SteamAPI_ManualDispatch_GetNextCallback"](pipe, message):
            try:
                reached, deliveries = self._read(message)
            finally:
                native["SteamAPI_ManualDispatch_FreeLastCallback"](pipe)
            dispatched += reached
            for deliver in deliveries:
                try:
                    deliver()
                except Exception as error:
                    errors.append(error)
        if errors:
            raise ExceptionGroup("callback handlers raised exceptions", errors)
        return dispatched

    def _read(self, message: CallbackMsg_t) -> tuple[bool, list[Callable[[], object]]]:
        """Copy what the message carries while it is valid.

        Returns whether it reached a subscriber or a pending call result, and the calls that
        deliver it once it is freed.
        """
        callback_id, size = message.m_iCallback, message.m_cubParam
        struct = _STRUCTS.get(callback_id)
        if struct is None:
            return False, []
        if size != ctypes.sizeof(struct):
            if callback_id not in self._warned:
                self._warned.add(callback_id)
                warnings.warn(
                    f"skipping callback {callback_id} ({struct.__name__}): Steam sent {size} "
                    f"bytes, steamctypes expects {ctypes.sizeof(struct)}. The steam_api library "
                    f"may not be from Steamworks SDK {SDK_VERSION}.",
                    SteamWarning,
                    stacklevel=5,  # the caller of run_callbacks() or CallResult.wait()
                )
            return False, []
        handlers = tuple(self._subscribers.get(struct, ()))
        completes_call = callback_id == _COMPLETED_ID
        if not handlers and not completes_call:
            return False, []
        data = struct.from_buffer_copy(ctypes.string_at(message.m_pubParam, size))
        deliveries: list[Callable[[], object]] = [functools.partial(h, data) for h in handlers]
        pending = self._pending.pop(data.m_hAsyncCall, None) if completes_call else None
        if pending is not None:
            deliveries += self._complete(data.m_hAsyncCall, pending)
        return bool(handlers) or pending is not None, deliveries

    def _complete(self, handle: int, pending: _Pending[Any]) -> list[Callable[[], object]]:
        """Fetch the result of a completed call and settle it; return its done callbacks."""
        result = pending.struct()
        failed = ctypes.c_bool()
        fetched = self.native["SteamAPI_ManualDispatch_GetAPICallResult"](
            self._pipe,
            handle,
            ctypes.addressof(result),
            ctypes.sizeof(result),
            _id_of(pending.struct),
            failed,
        )
        if fetched and not failed.value:
            return pending.finish(result, None)
        utils = self.native[ACCESSORS["ISteamUtils"]["user"]]()
        reason = self.native["SteamAPI_ISteamUtils_GetAPICallFailureReason"](utils, handle)
        return pending.finish(None, CallResultError(reason))
