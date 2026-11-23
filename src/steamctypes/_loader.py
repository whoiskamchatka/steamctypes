"""Find and load the steam_api shared library."""

import ctypes
import os
import platform
import sys
from pathlib import Path

from steamctypes.errors import IncompatibleLibraryError, LibraryNotFoundError, SteamError

ENV_VAR = "STEAMCTYPES_LIB"

# The SDK's redistributable_bin folder for sys.platform and the lower-case platform.machine().
# The macOS library is universal.
_FOLDERS = {
    ("win32", "amd64"): "win64",
    ("linux", "x86_64"): "linux64",
    ("linux", "aarch64"): "linuxarm64",
    ("darwin", "x86_64"): "osx",
    ("darwin", "arm64"): "osx",
}
_NAMES = {
    "win64": "steam_api64.dll",
    "linux64": "libsteam_api.so",
    "linuxarm64": "libsteam_api.so",
    "osx": "libsteam_api.dylib",
}


def library_folder() -> str:
    """The redistributable_bin folder of the library this platform loads."""
    if sys.maxsize <= 2**32:
        raise SteamError("steamctypes needs a 64-bit Python")
    machine = platform.machine()
    folder = _FOLDERS.get((sys.platform, machine.lower()))
    if folder is None:
        raise SteamError(f"steamctypes does not support {sys.platform} on {machine}")
    return folder


def library_name() -> str:
    return _NAMES[library_folder()]


def _search_folders() -> list[Path]:
    folders: list[Path] = []
    if getattr(sys, "frozen", False):
        folders.append(Path(sys.executable).parent)
    if bundle := getattr(sys, "_MEIPASS", None):
        folders.append(Path(bundle))
    if script := getattr(sys.modules.get("__main__"), "__file__", None):
        folders.append(Path(script).resolve().parent)
    return list(dict.fromkeys(folders))


def _only(location: Path, name: str, source: str) -> Path:
    candidate = location / name if location.is_dir() else location
    if not candidate.is_file():
        raise LibraryNotFoundError(f"cannot find {name} at {candidate} ({source})")
    return candidate.resolve()


def find_library(path: str | os.PathLike[str] | None = None) -> Path:
    """The library at an explicit path, else at STEAMCTYPES_LIB, else next to the program.

    An explicit or environment path may name the file or its folder, and is the only place
    looked: a wrong path fails instead of silently loading another library. Otherwise the
    folders of a frozen executable, its PyInstaller bundle and the main script are searched.
    The current directory is not, so that a library planted there is never loaded.
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
    if tried:
        searched = "tried, in order:\n" + "\n".join(f"  {candidate}" for candidate in tried)
    else:
        searched = "there is no executable or script folder to search."
    raise LibraryNotFoundError(f"cannot find {name}; {searched}\nPass lib_path or set {ENV_VAR}.")


def load_library(path: Path) -> ctypes.CDLL:
    try:
        return ctypes.CDLL(str(path.resolve()))
    except OSError as error:
        raise IncompatibleLibraryError(f"cannot load {path}: {error}") from error
