import re
import sys
from pathlib import Path

import pytest

from steamctypes._loader import ENV_VAR, find_library, library_name
from steamctypes.errors import LibraryNotFoundError


def test_find_library_search_order(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    name = library_name()
    keys = ("explicit", "env", "exe", "bundle", "script", "cwd")
    folders = {key: tmp_path / key for key in keys}
    for folder in folders.values():
        folder.mkdir()
        (folder / name).write_bytes(b"")
    monkeypatch.setenv(ENV_VAR, str(folders["env"]))
    # A one-file PyInstaller game: the executable's folder, then the unpacked bundle.
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(folders["exe"] / "game.exe"))
    monkeypatch.setattr(sys, "_MEIPASS", str(folders["bundle"]), raising=False)
    monkeypatch.setattr(sys.modules["__main__"], "__file__", str(folders["script"] / "game.py"))
    monkeypatch.chdir(folders["cwd"])

    def found(path: Path | None = None) -> str:
        return find_library(path).parent.name

    # An explicit path, else STEAMCTYPES_LIB, is the only place looked: no fallback.
    assert found(folders["explicit"] / name) == "explicit"
    assert found() == "env"
    missing = folders["explicit"] / "missing"
    with pytest.raises(LibraryNotFoundError, match=re.escape(f"{missing} (given explicitly)")):
        find_library(missing)
    monkeypatch.setenv(ENV_VAR, str(missing))
    with pytest.raises(LibraryNotFoundError, match=re.escape(f"{missing} (set in {ENV_VAR})")):
        find_library()

    # Without either, the program's folders are searched in order, never the current directory.
    monkeypatch.delenv(ENV_VAR)
    for key in ("exe", "bundle", "script"):
        assert found() == key
        (folders[key] / name).unlink()
    with pytest.raises(LibraryNotFoundError) as error:
        find_library()
    message = str(error.value)
    tried = [folders["exe"] / name, folders["bundle"] / name, folders["script"].resolve() / name]
    positions = [message.find(str(path)) for path in tried]
    assert -1 not in positions
    assert positions == sorted(positions)
    assert str(folders["cwd"]) not in message

    # In a REPL there is nothing to search.
    monkeypatch.setattr(sys, "frozen", False)
    monkeypatch.delattr(sys, "_MEIPASS")
    monkeypatch.delattr(sys.modules["__main__"], "__file__")
    with pytest.raises(
        LibraryNotFoundError, match=f"(?s)no executable or script folder.*{ENV_VAR}"
    ):
        find_library()
