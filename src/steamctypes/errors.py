"""Exceptions and warnings raised by steamctypes."""


class SteamError(Exception):
    """Base class of every steamctypes error."""


class LibraryNotFoundError(SteamError):
    """The steam_api library was not found."""


class IncompatibleLibraryError(SteamError):
    """The steam_api library cannot be used with this version of steamctypes."""


class SteamInitError(SteamError):
    """Steam refused to initialize. `result` is the ESteamAPIInitResult code."""

    def __init__(self, result: int, message: str) -> None:
        super().__init__(f"Steam initialization failed with result {result}: {message}")
        self.result = result
        self.message = message


class NoSteamClientError(SteamInitError):
    """No running, logged-in Steam client was found."""


class VersionMismatchError(SteamInitError):
    """The running Steam client does not support the interface versions of this SDK."""


class CallResultError(SteamError):
    """An asynchronous Steam API call failed. `reason` is the ESteamAPICallFailure code."""

    def __init__(self, reason: int) -> None:
        super().__init__(f"the Steam API call failed with reason {reason}")
        self.reason = reason


class SteamWarning(UserWarning):
    """Something works but may misbehave, such as a steam_api library from another SDK version."""
