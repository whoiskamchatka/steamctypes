import pickle
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
from tests.fake_steam import FakeSteamLibrary


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
    assert fake.init_versions == list(INIT_INTERFACE_VERSIONS)

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
        # Errors cross process boundaries, for example from a process pool worker.
        restored = pickle.loads(pickle.dumps(raised.value))
        assert (type(restored), str(restored)) == (error, str(raised.value))
        assert (restored.result, restored.message) == (code, raised.value.message)
    assert "SteamAPI_ManualDispatch_Init" not in fake.calls


def test_one_session_per_process(fake: FakeSteamLibrary) -> None:
    steam = Steam()
    with pytest.raises(SteamError, match="already initialized"):
        Steam()
    steam.shutdown()
    with pytest.raises(SteamError, match="again after a shutdown"):
        Steam()
    assert fake.calls.count("SteamInternal_SteamAPI_Init") == 1
