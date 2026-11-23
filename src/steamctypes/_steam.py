"""Start and stop Steam."""

import atexit
import ctypes
import operator
import os
import threading
from collections.abc import Callable
from typing import Self, TypeVar

from steamctypes._dispatch import CallResult, Dispatcher, callback_id_of
from steamctypes._generated import INIT_INTERFACE_VERSIONS, typedefs
from steamctypes._generated.enums import ESteamAPIInitResult
from steamctypes._loader import find_library, load_library
from steamctypes._native import Native, check_compatible
from steamctypes.errors import (
    NoSteamClientError,
    SteamError,
    SteamInitError,
    VersionMismatchError,
)

T = TypeVar("T", bound=ctypes.Structure)
R = TypeVar("R")

# NUL-terminated version strings, ended by an empty one.
_INIT_VERSIONS = b"".join(version.encode() + b"\0" for version in INIT_INTERFACE_VERSIONS) + b"\0"
_INIT_ERRORS: dict[int, type[SteamInitError]] = {
    ESteamAPIInitResult.k_ESteamAPIInitResult_NoSteamClient: NoSteamClientError,
    ESteamAPIInitResult.k_ESteamAPIInitResult_VersionMismatch: VersionMismatchError,
}

_lock = threading.Lock()
# The dispatcher of the live session, if any. It holds the session's library.
_active: Dispatcher | None = None
# Valve does not document initializing again after a shutdown, so a process gets one session.
_initialized = False


def _open_native(lib_path: str | os.PathLike[str] | None) -> Native:
    path = find_library(lib_path)
    library = load_library(path)
    check_compatible(library, path)
    return Native(library)


def async_call(function: str, struct: type[T], *args: object) -> CallResult[T]:
    """Call a flat function that returns a SteamAPICall_t; for steamctypes internals."""
    with _lock:
        dispatcher = _active
    if dispatcher is None:
        raise SteamError("Steam is not initialized")
    return dispatcher.async_call(function, struct, *args)


class Steam:
    """The Steamworks session of this process. Use it in a with block or call shutdown()."""

    def __init__(self, lib_path: str | os.PathLike[str] | None = None) -> None:
        global _active, _initialized
        with _lock:
            if _active is not None:
                raise SteamError("Steam is already initialized in this process")
            if _initialized:
                raise SteamError("Steam cannot be initialized again after a shutdown")
            native = _open_native(lib_path)
            message = typedefs.SteamErrMsg()
            result = native["SteamInternal_SteamAPI_Init"](_INIT_VERSIONS, message)
            if result != ESteamAPIInitResult.k_ESteamAPIInitResult_OK:
                text = message.value.decode("utf-8", errors="replace")
                raise _INIT_ERRORS.get(result, SteamInitError)(result, text)
            native["SteamAPI_ManualDispatch_Init"]()
            self._pipe: int = native["SteamAPI_GetHSteamPipe"]()
            self._user: int = native["SteamAPI_GetHSteamUser"]()
            self._dispatcher: Dispatcher | None = Dispatcher(native, self._pipe)
            _active, _initialized = self._dispatcher, True
            atexit.register(self._shut_down)

    @property
    def pipe(self) -> int:
        """The HSteamPipe handle."""
        return self._pipe

    @property
    def user(self) -> int:
        """The HSteamUser handle."""
        return self._user

    def run_callbacks(self) -> int:
        """Deliver queued callbacks and call results; call it every frame.

        Returns how many callbacks reached a subscriber or a call result. If handlers raise,
        the rest of the frame is still delivered, then an ExceptionGroup is raised. A frame
        running on another thread, for example in CallResult.wait(), finishes first.
        """
        return self._live().run()

    def on(self, struct: type[T]) -> Callable[[Callable[[T], R]], Callable[[T], R]]:
        """Decorator that subscribes a handler to a callback struct; undo it with off().

        Pointer fields in the struct are valid only while the handler runs.
        Handlers run on the thread that runs the frame, possibly one blocked in CallResult.wait().
        """
        callback_id_of(struct)

        def subscribe(handler: Callable[[T], R]) -> Callable[[T], R]:
            self._live().subscribe(struct, handler)
            return handler

        return subscribe

    def off(self, struct: type[T], handler: Callable[[T], object]) -> None:
        self._live().unsubscribe(struct, handler)

    def shutdown(self) -> None:
        """Shut Steam down. Later calls do nothing.

        Pending call results fail with SteamError and their done callbacks run afterwards; if
        any of them raise, an ExceptionGroup is raised.
        """
        errors: list[Exception] = []
        for callback in self._shut_down():
            try:
                callback()
            except Exception as error:
                errors.append(error)
        if errors:
            raise ExceptionGroup("done callbacks raised exceptions", errors)

    def _shut_down(self) -> list[Callable[[], object]]:
        """Shut down and return the done callbacks of the failed calls, without running them.

        This is the atexit hook: user code must not run while the interpreter exits.
        """
        global _active
        with _lock:
            dispatcher = self._dispatcher
            if dispatcher is None:
                return []
            if dispatcher.in_handler():
                raise SteamError("Steam cannot be shut down from inside a callback handler")
            self._dispatcher = _active = None
            atexit.unregister(self._shut_down)
        callbacks = dispatcher.close()
        dispatcher.native["SteamAPI_Shutdown"]()
        return callbacks

    def _live(self) -> Dispatcher:
        if self._dispatcher is None:
            raise SteamError("Steam has been shut down")
        return self._dispatcher

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.shutdown()


def restart_app_if_necessary(app_id: int, lib_path: str | os.PathLike[str] | None = None) -> bool:
    """Relaunch the game through Steam if needed. If this returns True, exit immediately."""
    # ctypes would silently keep the low 32 bits and ask about another app.
    app_id = operator.index(app_id)
    if not 0 <= app_id <= 0xFFFF_FFFF:
        raise ValueError(f"an app id is an unsigned 32-bit number, not {app_id}")
    with _lock:
        native = _active.native if _active is not None else _open_native(lib_path)
    return bool(native["SteamAPI_RestartAppIfNecessary"](app_id))
