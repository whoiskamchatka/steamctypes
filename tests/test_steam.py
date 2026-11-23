import atexit
import os
from collections.abc import Callable

import pytest

from steamctypes import (
    NoSteamClientError,
    Steam,
    SteamError,
    SteamInitError,
    VersionMismatchError,
)
from steamctypes._generated import INIT_INTERFACE_VERSIONS
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
    library = FakeSteamLibrary()

    def open_fake(lib_path: str | os.PathLike[str] | None) -> Native:
        return Native(library)

    monkeypatch.setattr("steamctypes._steam._open_native", open_fake)
    monkeypatch.setattr("steamctypes._steam._active", None)
    monkeypatch.setattr("steamctypes._steam._initialized", False)
    return library


def test_init_stores_handles_and_shuts_down_once(
    fake: FakeSteamLibrary, exit_hooks: list[Callable[[], None]]
) -> None:
    fake.pipe, fake.user = 7, 9
    steam = Steam()
    assert (steam.pipe, steam.user) == (7, 9)
    assert fake.calls == [
        "SteamInternal_SteamAPI_Init",
        "SteamAPI_ManualDispatch_Init",
        "SteamAPI_GetHSteamPipe",
        "SteamAPI_GetHSteamUser",
    ]
    assert fake.init_versions == "\0".join(INIT_INTERFACE_VERSIONS).encode() + b"\0\0"

    [hook] = exit_hooks
    steam.shutdown()
    steam.shutdown()
    assert exit_hooks == []
    hook()
    assert fake.calls.count("SteamAPI_Shutdown") == 1


def test_init_failures_carry_steam_message(fake: FakeSteamLibrary) -> None:
    cases = [
        (1, SteamInitError, b"Generic failure"),
        (2, NoSteamClientError, "Клиент Steam не запущен".encode()),
        (3, VersionMismatchError, b"bad \xff byte"),
    ]
    for code, error, message in cases:
        fake.init_result, fake.init_message = code, message
        with pytest.raises(error) as raised:
            Steam()
        assert type(raised.value) is error
        assert raised.value.result == code
        assert raised.value.message == message.decode("utf-8", errors="replace")
    assert "SteamAPI_ManualDispatch_Init" not in fake.calls


def test_one_session_per_process(fake: FakeSteamLibrary) -> None:
    steam = Steam()
    with pytest.raises(SteamError, match="already initialized"):
        Steam()
    steam.shutdown()
    with pytest.raises(SteamError, match="again after a shutdown"):
        Steam()
    assert fake.calls.count("SteamInternal_SteamAPI_Init") == 1
