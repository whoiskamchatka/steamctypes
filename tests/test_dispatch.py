from collections.abc import Iterator

import pytest

from steamctypes import CallResult, CallResultError, Steam, SteamError, SteamWarning
from steamctypes._generated.enums import ESteamAPICallFailure
from steamctypes._generated.structs import LeaderboardFindResult_t, PersonaStateChange_t
from steamctypes._steam import call_result
from tests.fake_steam import FakeSteamLibrary

PERSONA = PersonaStateChange_t.k_iCallback
UNKNOWN_ID = 1_040_044  # Steam sends ids like this one that are not in steam_api.json


@pytest.fixture
def steam(fake: FakeSteamLibrary) -> Iterator[Steam]:
    session = Steam()
    yield session
    session.shutdown()


def persona_change(steam_id: int) -> bytes:
    return bytes(PersonaStateChange_t(m_ulSteamID=steam_id, m_nChangeFlags=1))


def test_callbacks_reach_subscribers_as_copies(steam: Steam, fake: FakeSteamLibrary) -> None:
    received: list[PersonaStateChange_t] = []
    steam.on(PersonaStateChange_t)(received.append)
    fake.post(PERSONA, persona_change(42))
    fake.post(UNKNOWN_ID, bytes(784))
    fake.post(PERSONA, persona_change(43)[:-1])
    fake.post(PERSONA, persona_change(44)[:-1])

    with pytest.warns(SteamWarning, match="Steam sent") as warned:
        assert steam.run_callbacks() == 1
    assert len(warned) == 1
    assert [bytes(data) for data in received] == [persona_change(42)]
    assert fake.delivered == fake.freed == 4


def test_raising_handler_does_not_stop_the_frame(steam: Steam, fake: FakeSteamLibrary) -> None:
    calls: list[str] = []

    @steam.on(PersonaStateChange_t)
    def failing(data: PersonaStateChange_t) -> None:
        calls.append("failing")
        raise RuntimeError("handler failed")

    @steam.on(PersonaStateChange_t)
    def once(data: PersonaStateChange_t) -> None:
        calls.append("once")
        steam.off(PersonaStateChange_t, once)

    fake.post(PERSONA, persona_change(1))
    fake.post(PERSONA, persona_change(2))
    with pytest.raises(ExceptionGroup) as group:
        steam.run_callbacks()
    assert calls == ["failing", "once", "failing"]
    assert [str(error) for error in group.value.exceptions] == ["handler failed"] * 2
    assert fake.delivered == fake.freed == 2


def test_call_results(steam: Steam, fake: FakeSteamLibrary) -> None:
    found = call_result(11, LeaderboardFindResult_t)
    done: list[CallResult[LeaderboardFindResult_t]] = []
    found.add_done_callback(done.append)
    fake.complete_call(11, LeaderboardFindResult_t(m_hSteamLeaderboard=5, m_bLeaderboardFound=1))
    network_failure = ESteamAPICallFailure.k_ESteamAPICallFailureNetworkFailure
    failing = call_result(12, LeaderboardFindResult_t)
    fake.complete_call(12, LeaderboardFindResult_t(), failed=True, reason=network_failure)

    assert steam.run_callbacks() == 2
    assert found.result().m_hSteamLeaderboard == 5
    assert done == [found]
    with pytest.raises(CallResultError) as failure:
        failing.result()
    assert failure.value.reason == network_failure
    with pytest.raises(CallResultError):
        call_result(0, LeaderboardFindResult_t).result()

    slow = call_result(13, LeaderboardFindResult_t)
    fake.complete_call(13, LeaderboardFindResult_t(m_hSteamLeaderboard=7), frames=3)
    frames = fake.frames
    assert slow.wait(timeout=5).m_hSteamLeaderboard == 7
    assert fake.frames - frames == 4

    pending = call_result(14, LeaderboardFindResult_t)
    with pytest.raises(SteamError, match="not completed"):
        pending.result()
    steam.shutdown()
    with pytest.raises(SteamError, match="shut down"):
        pending.result()
