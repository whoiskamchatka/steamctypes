"""A stand-in for the steam_api library, so tests never touch Steam."""

import ctypes
import time
from collections.abc import Callable
from typing import Any

from steamctypes._generated.callbacks import CALLBACKS
from steamctypes._generated.functions import ACCESSORS
from steamctypes._generated.structs import CallbackMsg_t, SteamAPICallCompleted_t

UTILS = 0x5E11  # what the fake ISteamUtils accessor returns
CALLBACK_IDS = {
    struct: callback_id for callback_id, structs in CALLBACKS.items() for struct in structs
}


class FakeFunction:
    """One export: records its calls and accepts the restype and argtypes steamctypes sets."""

    def __init__(self, calls: list[str], name: str, body: Callable[..., Any]) -> None:
        self.calls = calls
        self.name = name
        self.body = body
        self.restype: object = None
        self.argtypes: object = ()

    def __call__(self, *args: Any) -> Any:
        self.calls.append(self.name)
        return self.body(*args)


class FakeSteamLibrary:
    """The functions steamctypes calls, with configurable results and a callback queue."""

    def __init__(self) -> None:
        self.calls: list[str] = []
        self.init_result = 0
        self.init_message = b""
        self.init_versions = b""
        self.pipe = 1
        self.user = 1
        self.restart = False
        self.frames = 0
        self.queue: list[tuple[int, int, bytes]] = []  # frame it is due, callback id, payload
        self.call_results: dict[int, tuple[bytes, bool, int]] = {}  # payload, failed, reason
        self.payload: ctypes.Array[ctypes.c_char] | None = None  # the message being dispatched
        self.owned: list[ctypes.Array[ctypes.c_char]] = []  # what the next free invalidates
        self.delivered = 0
        self.freed = 0
        self.frame_delay = 0.0
        self.next_handle = 100
        self.during_call: Callable[[int], None] | None = None
        self.functions: dict[str, Callable[..., Any]] = {
            "SteamInternal_SteamAPI_Init": self.init,
            "SteamAPI_ManualDispatch_Init": lambda: None,
            "SteamAPI_GetHSteamPipe": lambda: self.pipe,
            "SteamAPI_GetHSteamUser": lambda: self.user,
            "SteamAPI_RestartAppIfNecessary": self.restart_app,
            "SteamAPI_Shutdown": lambda: None,
            "SteamAPI_ManualDispatch_RunFrame": self.run_frame,
            "SteamAPI_ManualDispatch_GetNextCallback": self.next_callback,
            "SteamAPI_ManualDispatch_FreeLastCallback": self.free_last_callback,
            "SteamAPI_ManualDispatch_GetAPICallResult": self.get_call_result,
            ACCESSORS["ISteamUtils"]["user"]: lambda: UTILS,
            "SteamAPI_ISteamUtils_GetAPICallFailureReason": self.failure_reason,
            "SteamAPI_ISteamUserStats_FindLeaderboard": self.find_leaderboard,
        }

    def __getattr__(self, name: str) -> FakeFunction:
        if name not in self.functions:
            raise AttributeError(name)
        return FakeFunction(self.calls, name, self.functions[name])

    def post(self, callback_id: int, payload: bytes, frames: int = 0) -> None:
        """Queue a callback for the RunFrame `frames` frames after the next one."""
        self.queue.append((self.frames + 1 + frames, callback_id, payload))

    def steam_owned(self, data: bytes) -> int:
        """The address of memory Steam owns until the next FreeLastCallback."""
        buffer = ctypes.create_string_buffer(data, len(data))
        self.owned.append(buffer)
        return ctypes.addressof(buffer)

    def complete_call(
        self,
        handle: int,
        result: ctypes.Structure,
        failed: bool = False,
        reason: int = -1,
        frames: int = 0,
    ) -> None:
        payload = bytes(result)
        self.call_results[handle] = (payload, failed, reason)
        completed = SteamAPICallCompleted_t(
            m_hAsyncCall=handle, m_iCallback=CALLBACK_IDS[type(result)], m_cubParam=len(payload)
        )
        self.post(SteamAPICallCompleted_t.k_iCallback, bytes(completed), frames)

    def init(self, versions: bytes, message: ctypes.Array[ctypes.c_char]) -> int:
        self.init_versions = versions
        message.value = self.init_message
        return self.init_result

    def restart_app(self, app_id: int) -> bool:
        return self.restart

    def run_frame(self, pipe: int) -> None:
        time.sleep(self.frame_delay)
        self.frames += 1

    def find_leaderboard(self, stats: int | None, name: bytes) -> int:
        handle = self.next_handle
        self.next_handle += 1
        if self.during_call is not None:
            self.during_call(handle)
        return handle

    def next_callback(self, pipe: int, message: CallbackMsg_t) -> bool:
        assert self.payload is None, "GetNextCallback before the last callback was freed"
        due = next((entry for entry in self.queue if entry[0] <= self.frames), None)
        if due is None:
            return False
        self.queue.remove(due)
        _, callback_id, payload = due
        self.payload = ctypes.create_string_buffer(payload, len(payload))
        message.m_hSteamUser = self.user
        message.m_iCallback = callback_id
        message.m_pubParam = ctypes.addressof(self.payload)
        message.m_cubParam = len(payload)
        self.delivered += 1
        return True

    def free_last_callback(self, pipe: int) -> None:
        assert self.payload is not None, "FreeLastCallback without a callback"
        for buffer in (self.payload, *self.owned):
            ctypes.memset(buffer, 0xEE, len(buffer))  # anything not copied is now garbage
        self.payload = None
        self.owned.clear()
        self.freed += 1

    def get_call_result(
        self,
        pipe: int,
        handle: int,
        buffer: int,
        size: int,
        expected_id: int,
        failed: ctypes.c_bool,
    ) -> bool:
        if handle not in self.call_results:
            return False
        payload, call_failed, _ = self.call_results[handle]
        if size != len(payload):
            return False
        ctypes.memmove(buffer, payload, size)
        failed.value = call_failed
        return True

    def failure_reason(self, utils: int, handle: int) -> int:
        assert utils == UTILS
        return self.call_results[handle][2]
