"""Find and load the steam_api shared library."""

import ctypes
import os
import sys
from pathlib import Path

from steamctypes.errors import IncompatibleLibraryError, LibraryNotFoundError, SteamError

ENV_VAR = "STEAMCTYPES_LIB"


def library_name() -> str:
    if sys.maxsize <= 2**32:
        raise SteamError("steamctypes needs a 64-bit Python")
    if sys.platform == "win32":
        return "steam_api64.dll"
    if sys.platform.startswith("linux"):
        return "libsteam_api.so"
    if sys.platform == "darwin":
        return "libsteam_api.dylib"
    raise SteamError(f"steamctypes does not support the platform {sys.platform!r}")


def _search_folders() -> list[Path]:
    folders: list[Path] = []
    if getattr(sys, "frozen", False):
        folders.append(Path(sys.executable).parent)
    if bundle := getattr(sys, "_MEIPASS", None):
        folders.append(Path(bundle))
    if script := getattr(sys.modules.get("__main__"), "__file__", None):
        folders.append(Path(script).resolve().parent)
    folders.append(Path.cwd())
    return list(dict.fromkeys(folders))


def _only(location: Path, name: str, source: str) -> Path:
    candidate = location / name if location.is_dir() else location
    if not candidate.is_file():
        raise LibraryNotFoundError(f"cannot find {name} at {candidate} ({source})")
    return candidate.resolve()


def find_library(path: str | os.PathLike[str] | None = None) -> Path:
    """The library at an explicit path, else at STEAMCTYPES_LIB, else in the usual folders.

    An explicit or environment path may name the file or its folder, and is the only place
    looked: a wrong path fails instead of silently loading another library.
    """
    name = library_name()
    if path is not None:
        return _only(Path(path), name, "given explicitly")
    if env_path := os.environ.get(ENV_VAR):
        return _only(Path(env_path), name, f"set in {ENV_VAR}")

    tried = [folder / name for folder in _search_folders()]
    for candidate in tried:
        if candidate.is_file():
            return candidate.resolve()
    listing = "\n".join(f"  {candidate}" for candidate in tried)
    raise LibraryNotFoundError(f"cannot find {name}; tried, in order:\n{listing}")


def load_library(path: Path) -> ctypes.CDLL:
    try:
        return ctypes.CDLL(str(path.resolve()))
    except OSError as error:
        raise IncompatibleLibraryError(f"cannot load {path}: {error}") from error
