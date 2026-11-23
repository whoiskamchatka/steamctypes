"""Bind the generated prototypes to a loaded steam_api library."""

import ctypes
import hashlib
import warnings
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, Final

from steamctypes._generated import LIBRARY_SHA256, SDK_VERSION, typedefs
from steamctypes._generated.functions import PROTOTYPES, Prototype
from steamctypes._loader import library_name
from steamctypes.errors import IncompatibleLibraryError, SteamWarning

# The global functions are not in steam_api.json. Signatures from steam_api.h and
# steam_api_internal.h; the init result is an ESteamAPIInitResult.
GLOBAL_PROTOTYPES: Final[Mapping[str, Prototype]] = {
    "SteamInternal_SteamAPI_Init": (
        ctypes.c_int,
        (ctypes.c_char_p, ctypes.POINTER(typedefs.SteamErrMsg)),
    ),
    "SteamAPI_Shutdown": (None, ()),
    "SteamAPI_RestartAppIfNecessary": (ctypes.c_bool, (typedefs.uint32,)),
    "SteamAPI_ManualDispatch_Init": (None, ()),
    "SteamAPI_GetHSteamPipe": (typedefs.HSteamPipe, ()),
    "SteamAPI_GetHSteamUser": (typedefs.HSteamUser, ()),
}
_PROTOTYPES: Final[Mapping[str, Prototype]] = {**PROTOTYPES, **GLOBAL_PROTOTYPES}


class Native:
    """The flat API of a loaded library. Each function gets its prototype on first use."""

    def __init__(self, library: object) -> None:
        self._library = library
        self._bound: dict[str, Callable[..., Any]] = {}

    def __getitem__(self, name: str) -> Callable[..., Any]:
        function = self._bound.get(name)
        if function is None:
            restype, argtypes = _PROTOTYPES[name]
            function = getattr(self._library, name)
            function.restype = restype
            function.argtypes = argtypes
            self._bound[name] = function
        return function


def check_compatible(library: object, path: Path) -> None:
    """Fail if the library lacks any function of our SDK; warn if it is not our SDK's file."""
    missing = [name for name in _PROTOTYPES if not hasattr(library, name)]
    if missing:
        raise IncompatibleLibraryError(
            f"{path} is not the steam_api library from Steamworks SDK {SDK_VERSION}: "
            f"{len(missing)} of {len(_PROTOTYPES)} functions are missing, "
            f"for example {', '.join(missing[:3])}"
        )
    with path.open("rb") as f:
        digest = hashlib.file_digest(f, "sha256").hexdigest()
    if digest != LIBRARY_SHA256[library_name()]:
        warnings.warn(
            f"{path} differs from the steam_api library in Steamworks SDK {SDK_VERSION}. It has "
            "every function steamctypes needs, but if it comes from another SDK version, struct "
            "layouts may differ.",
            SteamWarning,
            stacklevel=2,
        )
