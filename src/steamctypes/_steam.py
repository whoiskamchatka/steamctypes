"""Start and stop Steam."""

import atexit
import os
import threading
from typing import Self

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

# NUL-terminated version strings, ended by an empty one.
_INIT_VERSIONS = b"".join(version.encode() + b"\0" for version in INIT_INTERFACE_VERSIONS) + b"\0"
_INIT_ERRORS: dict[int, type[SteamInitError]] = {
    ESteamAPIInitResult.k_ESteamAPIInitResult_NoSteamClient: NoSteamClientError,
    ESteamAPIInitResult.k_ESteamAPIInitResult_VersionMismatch: VersionMismatchError,
}

_lock = threading.Lock()
# The library of the live session, if any.
_active: Native | None = None
# Valve does not document initializing again after a shutdown, so a process gets one session.
_initialized = False


def _open_native(lib_path: str | os.PathLike[str] | None) -> Native:
    path = find_library(lib_path)
    library = load_library(path)
    check_compatible(library, path)
    return Native(library)


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
            self._native: Native | None = native
            self._pipe: int = native["SteamAPI_GetHSteamPipe"]()
            self._user: int = native["SteamAPI_GetHSteamUser"]()
            _active, _initialized = native, True
            atexit.register(self.shutdown)

    @property
    def pipe(self) -> int:
        """The HSteamPipe handle."""
        return self._pipe

    @property
    def user(self) -> int:
        """The HSteamUser handle."""
        return self._user

    def shutdown(self) -> None:
        """Shut Steam down. Later calls do nothing."""
        global _active
        with _lock:
            native, self._native = self._native, None
            if native is None:
                return
            atexit.unregister(self.shutdown)
            _active = None
            native["SteamAPI_Shutdown"]()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.shutdown()


def restart_app_if_necessary(app_id: int, lib_path: str | os.PathLike[str] | None = None) -> bool:
    """Relaunch the game through Steam if needed. If this returns True, exit immediately."""
    with _lock:
        native = _active if _active is not None else _open_native(lib_path)
    return bool(native["SteamAPI_RestartAppIfNecessary"](app_id))
