"""A stand-in for the steam_api library, so tests never touch Steam."""

import ctypes
from collections.abc import Callable
from typing import Any


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
    """The global functions steamctypes calls, with configurable results."""

    def __init__(self) -> None:
        self.calls: list[str] = []
        self.init_result = 0
        self.init_message = b""
        self.init_versions = b""
        self.pipe = 1
        self.user = 1
        self.restart = False
        self.functions: dict[str, Callable[..., Any]] = {
            "SteamInternal_SteamAPI_Init": self.init,
            "SteamAPI_ManualDispatch_Init": lambda: None,
            "SteamAPI_GetHSteamPipe": lambda: self.pipe,
            "SteamAPI_GetHSteamUser": lambda: self.user,
            "SteamAPI_RestartAppIfNecessary": self.restart_app,
            "SteamAPI_Shutdown": lambda: None,
        }

    def __getattr__(self, name: str) -> FakeFunction:
        if name not in self.functions:
            raise AttributeError(name)
        return FakeFunction(self.calls, name, self.functions[name])

    def init(self, versions: bytes, message: ctypes.Array[ctypes.c_char]) -> int:
        self.init_versions = versions
        message.value = self.init_message
        return self.init_result

    def restart_app(self, app_id: int) -> bool:
        return self.restart
