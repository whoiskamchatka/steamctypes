from pathlib import Path

import pytest

from steamctypes import restart_app_if_necessary
from steamctypes._generated.functions import PROTOTYPES
from steamctypes._loader import library_name
from steamctypes._native import check_compatible
from steamctypes.errors import IncompatibleLibraryError, SteamWarning
from tests.fake_steam import export


class FakeLibrary:
    """Has every function but the missing ones; only RestartAppIfNecessary can be called."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = set(missing)
        self.restart = export("SteamAPI_RestartAppIfNecessary", self.restart_app, [])

    def __getattr__(self, name: str) -> object:
        if name in self.missing:
            raise AttributeError(name)
        if name == "SteamAPI_RestartAppIfNecessary":
            return self.restart
        return object()  # enough for check_compatible; Native cannot bind it

    def restart_app(self, app_id: int) -> bool:
        return False


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
