"""Bind the generated prototypes to a loaded steam_api library."""

import hashlib
import warnings
from collections.abc import Callable
from pathlib import Path
from typing import Any

from steamctypes._generated import LIBRARY_SHA256, SDK_VERSION
from steamctypes._generated.functions import PROTOTYPES
from steamctypes._loader import library_folder
from steamctypes.errors import IncompatibleLibraryError, SteamWarning


class Native:
    """The flat API of a loaded library. Each function gets its prototype on first use."""

    def __init__(self, library: object) -> None:
        self._library = library
        self._bound: dict[str, Callable[..., Any]] = {}

    def __getitem__(self, name: str) -> Callable[..., Any]:
        function = self._bound.get(name)
        if function is None:
            restype, argtypes = PROTOTYPES[name]
            function = getattr(self._library, name)
            function.restype = restype
            function.argtypes = argtypes
            self._bound[name] = function
        return function


def check_compatible(library: object, path: Path) -> None:
    """Fail if the library lacks any function of our SDK; warn if it is not our SDK's file."""
    missing = [name for name in PROTOTYPES if not hasattr(library, name)]
    if missing:
        raise IncompatibleLibraryError(
            f"{path} is not the steam_api library from Steamworks SDK {SDK_VERSION}: "
            f"{len(missing)} of {len(PROTOTYPES)} functions are missing, "
            f"for example {', '.join(missing[:3])}"
        )
    with path.open("rb") as f:
        digest = hashlib.file_digest(f, "sha256").hexdigest()
    if digest != LIBRARY_SHA256[library_folder()]:
        warnings.warn(
            f"{path} differs from the steam_api library in Steamworks SDK {SDK_VERSION}. It has "
            "every function steamctypes needs, but if it comes from another SDK version, struct "
            "layouts may differ.",
            SteamWarning,
            stacklevel=4,  # past _open_native() and Steam() or restart_app_if_necessary()
        )
