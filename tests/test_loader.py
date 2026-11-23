import re
import sys
from pathlib import Path

import pytest

from steamctypes._loader import ENV_VAR, find_library, library_name
from steamctypes.errors import LibraryNotFoundError


def test_find_library_search_order(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    name = library_name()
    folders = {key: tmp_path / key for key in ("explicit", "env", "script", "cwd")}
    for folder in folders.values():
        folder.mkdir()
        (folder / name).write_bytes(b"")
    monkeypatch.setenv(ENV_VAR, str(folders["env"]))
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

    # Without either, the folders are searched in order.
    monkeypatch.delenv(ENV_VAR)
    assert found() == "script"
    (folders["script"] / name).unlink()
    assert found() == "cwd"
    (folders["cwd"] / name).unlink()
    with pytest.raises(LibraryNotFoundError) as error:
        find_library()
    message = str(error.value)
    tried = [folders["script"].resolve() / name, Path.cwd() / name]
    positions = [message.find(str(path)) for path in tried]
    assert -1 not in positions
    assert positions == sorted(positions)
