import atexit
import os
from collections.abc import Callable

import pytest

from steamctypes._native import Native
from tests.fake_steam import FakeSteamLibrary


@pytest.fixture
def exit_hooks(monkeypatch: pytest.MonkeyPatch) -> list[Callable[[], None]]:
    """Exit hooks registered during the test, kept out of the real atexit registry."""
    hooks: list[Callable[[], None]] = []
    monkeypatch.setattr(atexit, "register", hooks.append)
    monkeypatch.setattr(atexit, "unregister", hooks.remove)
    return hooks


@pytest.fixture
def fake(monkeypatch: pytest.MonkeyPatch, exit_hooks: list[Callable[[], None]]) -> FakeSteamLibrary:
    """A fake steam_api library that every Steam() in the test loads."""
    library = FakeSteamLibrary()

    def open_fake(lib_path: str | os.PathLike[str] | None) -> Native:
        return Native(library)

    monkeypatch.setattr("steamctypes._steam._open_native", open_fake)
    monkeypatch.setattr("steamctypes._steam._active", None)
    monkeypatch.setattr("steamctypes._steam._initialized", False)
    return library
