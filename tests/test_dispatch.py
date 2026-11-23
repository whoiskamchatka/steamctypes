import ctypes
import pickle
import threading
import time
from collections.abc import Iterator

import pytest

from steamctypes import CallResult, CallResultError, Steam, SteamError, SteamWarning
from steamctypes._generated.enums import ESteamAPICallFailure
from steamctypes._generated.structs import (
    GSStatsUnloaded_t,
    HTML_StartRequest_t,
    LeaderboardFindResult_t,
    PersonaStateChange_t,
    SteamAPICallCompleted_t,
)
from steamctypes._steam import async_call
from tests.fake_steam import FakeSteamLibrary

PERSONA = PersonaStateChange_t.k_iCallback
UNKNOWN_ID = 1_040_044  # Steam sends ids like this one that are not in steam_api.json
FIND = "SteamAPI_ISteamUserStats_FindLeaderboard"


@pytest.fixture
def steam(fake: FakeSteamLibrary) -> Iterator[Steam]:
    session = Steam()
    yield session
    session.shutdown()


def persona_change(steam_id: int) -> bytes:
    return bytes(PersonaStateChange_t(m_ulSteamID=steam_id, m_nChangeFlags=1))


def find(fake: FakeSteamLibrary) -> tuple[int, CallResult[LeaderboardFindResult_t]]:
    handle = fake.next_handle
    return handle, async_call(FIND, LeaderboardFindResult_t, None, b"Feet Traveled")


def test_callbacks_reach_subscribers_before_the_free(steam: Steam, fake: FakeSteamLibrary) -> None:
    requests: list[tuple[bytes, int]] = []

    @steam.on(HTML_StartRequest_t)
    def request(data: HTML_StartRequest_t) -> None:
        requests.append((ctypes.string_at(data.pchURL), fake.freed))

    received: list[PersonaStateChange_t] = []
    steam.on(PersonaStateChange_t)(received.append)
    url = fake.steam_owned(b"https://example.test/\0")
    fake.post(HTML_StartRequest_t.k_iCallback, bytes(HTML_StartRequest_t(pchURL=url)))
    fake.post(PERSONA, persona_change(42))
    fake.post(UNKNOWN_ID, bytes(784))
    fake.post(PERSONA, persona_change(43)[:-1])
    fake.post(PERSONA, persona_change(44)[:-1])

    with pytest.warns(SteamWarning, match="Steam sent") as warned:
        assert steam.run_callbacks() == 2
    assert [warning.filename for warning in warned] == [__file__]
    assert requests == [(b"https://example.test/", 0)]  # read before its message was freed
    assert [bytes(data) for data in received] == [persona_change(42)]
    assert fake.delivered == fake.freed == 5
    with pytest.raises(TypeError, match="GSStatsUnloaded_t"):
        steam.on(GSStatsUnloaded_t)


def test_raising_handler_does_not_stop_the_frame(steam: Steam, fake: FakeSteamLibrary) -> None:
    calls: list[tuple[str, int]] = []

    @steam.on(PersonaStateChange_t)
    def failing(data: PersonaStateChange_t) -> None:
        calls.append(("failing", fake.freed))
        raise RuntimeError("handler failed")

    @steam.on(PersonaStateChange_t)
    def once(data: PersonaStateChange_t) -> None:
        calls.append(("once", fake.freed))
        steam.off(PersonaStateChange_t, once)
        steam.on(PersonaStateChange_t)(lambda data: calls.append(("later", fake.freed)))

    fake.post(PERSONA, persona_change(1))
    fake.post(PERSONA, persona_change(2))
    with pytest.raises(ExceptionGroup) as group:
        steam.run_callbacks()
    # Each message is freed after its handlers, including the raising one. A handler subscribed
    # during the frame gets the next message.
    assert calls == [("failing", 0), ("once", 0), ("failing", 1), ("later", 1)]
    assert [str(error) for error in group.value.exceptions] == ["handler failed"] * 2
    assert fake.delivered == fake.freed == 2


def test_call_results(steam: Steam, fake: FakeSteamLibrary) -> None:
    handle, found = find(fake)
    done: list[CallResult[LeaderboardFindResult_t]] = []
    found.add_done_callback(done.append)
    fake.complete_call(
        handle, LeaderboardFindResult_t(m_hSteamLeaderboard=5, m_bLeaderboardFound=1)
    )
    network_failure = ESteamAPICallFailure.k_ESteamAPICallFailureNetworkFailure
    handle, failing = find(fake)
    fake.complete_call(handle, LeaderboardFindResult_t(), failed=True, reason=network_failure)

    assert steam.run_callbacks() == 2
    assert found.result().m_hSteamLeaderboard == 5
    assert done == [found]
    with pytest.raises(CallResultError) as failure:
        failing.result()
    assert failure.value.reason == network_failure
    restored = pickle.loads(pickle.dumps(failure.value))
    assert (restored.reason, str(restored)) == (network_failure, str(failure.value))
    fake.next_handle = 0  # k_uAPICallInvalid
    with pytest.raises(CallResultError):
        find(fake)[1].result()

    # The call completes while still inside the native call, and another thread is already
    # waiting to run a frame. That frame must not consume the completion before registration.
    pumped: list[int] = []
    pump = threading.Thread(target=lambda: pumped.append(steam.run_callbacks()))

    def complete_during_call(handle: int) -> None:
        fake.complete_call(handle, LeaderboardFindResult_t(m_hSteamLeaderboard=7))
        pump.start()
        time.sleep(0.05)

    fake.during_call = complete_during_call
    _, quick = find(fake)
    fake.during_call = None
    pump.join()
    assert pumped == [1]
    assert quick.result().m_hSteamLeaderboard == 7

    handle, slow = find(fake)
    fake.complete_call(handle, LeaderboardFindResult_t(m_hSteamLeaderboard=8), frames=3)
    frames = fake.frames
    assert slow.wait(timeout=5).m_hSteamLeaderboard == 8
    assert fake.frames - frames == 4

    mismatched: list[CallResult[LeaderboardFindResult_t]] = []
    for _ in range(2):
        handle, call = find(fake)
        mismatched.append(call)
        completed = SteamAPICallCompleted_t(
            m_hAsyncCall=handle, m_iCallback=LeaderboardFindResult_t.k_iCallback, m_cubParam=12
        )
        fake.post(SteamAPICallCompleted_t.k_iCallback, bytes(completed))
    with pytest.warns(SteamWarning, match="another SDK version") as warned:
        steam.run_callbacks()
    assert len(warned) == 1
    for call in mismatched:
        with pytest.raises(CallResultError, match="another SDK version") as failure:
            call.result()
        assert str(pickle.loads(pickle.dumps(failure.value))) == str(failure.value)


def test_wait_while_another_thread_dispatches(steam: Steam, fake: FakeSteamLibrary) -> None:
    fake.frame_delay = 0.005  # the pumping thread spends most of its time inside a frame
    stop = threading.Event()

    def pump() -> None:
        while not stop.is_set():
            steam.run_callbacks()

    handle, slow = find(fake)
    fake.complete_call(handle, LeaderboardFindResult_t(m_hSteamLeaderboard=9), frames=5)
    thread = threading.Thread(target=pump)
    thread.start()
    try:
        assert slow.wait(timeout=5).m_hSteamLeaderboard == 9
    finally:
        stop.set()
        thread.join()


def test_shutdown_settles_pending_calls(steam: Steam, fake: FakeSteamLibrary) -> None:
    _, pending = find(fake)
    with pytest.raises(SteamError, match="not completed"):
        pending.result()
    settled: list[str] = []

    def record(call: CallResult[LeaderboardFindResult_t]) -> None:
        with pytest.raises(SteamError, match="shut down"):
            call.result()
        settled.append(fake.calls[-1])

    def failing(call: CallResult[LeaderboardFindResult_t]) -> None:
        raise RuntimeError("done callback failed")

    pending.add_done_callback(record)
    pending.add_done_callback(failing)
    with pytest.raises(ExceptionGroup) as group:
        steam.shutdown()
    assert settled == ["SteamAPI_Shutdown"]  # the callbacks ran after it
    assert [str(error) for error in group.value.exceptions] == ["done callback failed"]
