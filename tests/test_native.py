from pathlib import Path
from types import SimpleNamespace

import pytest

from steamctypes._generated.functions import PROTOTYPES
from steamctypes._loader import library_name
from steamctypes._native import GLOBAL_PROTOTYPES, check_compatible
from steamctypes.errors import IncompatibleLibraryError, SteamWarning


class FakeLibrary:
    def __init__(self, missing: list[str]) -> None:
        self.missing = set(missing)

    def __getattr__(self, name: str) -> SimpleNamespace:
        if name in self.missing:
            raise AttributeError(name)
        return SimpleNamespace()


def test_check_compatible(tmp_path: Path) -> None:
    path = tmp_path / library_name()
    path.write_bytes(b"not the steam_api library")

    missing = [*list(PROTOTYPES)[:4], "SteamAPI_Shutdown"]
    total = len(PROTOTYPES) + len(GLOBAL_PROTOTYPES)
    with pytest.raises(IncompatibleLibraryError, match=rf"5 of {total} .*{missing[0]}"):
        check_compatible(FakeLibrary(missing), path)

    with pytest.warns(SteamWarning, match="differs from the steam_api library"):
        check_compatible(FakeLibrary([]), path)
