from collections.abc import Callable
from pathlib import Path

import pytest

from steamctypes import restart_app_if_necessary
from steamctypes._generated.functions import PROTOTYPES
from steamctypes._loader import library_name
from steamctypes._native import check_compatible
from steamctypes.errors import IncompatibleLibraryError, SteamWarning


class FakeLibrary:
    """Has every function but the missing ones; each returns 0."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = set(missing)

    def __getattr__(self, name: str) -> Callable[..., int]:
        if name in self.missing:
            raise AttributeError(name)
        return lambda *args: 0


def test_check_compatible(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    path = tmp_path / library_name()
    path.write_bytes(b"not the steam_api library")

    missing = [*list(PROTOTYPES)[:4], "SteamAPI_ISteamFriends_GetPersonaName"]
    with pytest.raises(IncompatibleLibraryError, match=rf"5 of {len(PROTOTYPES)} .*{missing[0]}"):
        check_compatible(FakeLibrary(missing), path)

    # A library from another SDK version still loads, with a warning at the caller's line.
    def load_library(path: Path) -> FakeLibrary:
        return FakeLibrary([])

    monkeypatch.setattr("steamctypes._steam.load_library", load_library)
    with pytest.warns(SteamWarning, match="differs from the steam_api library") as warned:
        assert not restart_app_if_necessary(480, path)
    assert [warning.filename for warning in warned] == [__file__]
    # ctypes would pass the low 32 bits, 480, on to Steam.
    with pytest.raises(ValueError, match="unsigned 32-bit"):
        restart_app_if_necessary(2**32 + 480, path)
