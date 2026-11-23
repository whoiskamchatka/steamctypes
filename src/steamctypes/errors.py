"""Exceptions and warnings raised by steamctypes."""


class SteamError(Exception):
    pass


class LibraryNotFoundError(SteamError):
    pass


class IncompatibleLibraryError(SteamError):
    """The steam_api library cannot be used with this version of steamctypes."""


class SteamInitError(SteamError):
    """Steam refused to initialize. `result` is the ESteamAPIInitResult code."""

    def __init__(self, result: int, message: str) -> None:
        # The constructor arguments go to args so that pickling can recreate the error.
        super().__init__(result, message)
        self.result = result
        self.message = message

    def __str__(self) -> str:
        return f"Steam initialization failed with result {self.result}: {self.message}"


class NoSteamClientError(SteamInitError):
    """No running, logged-in Steam client was found."""


class VersionMismatchError(SteamInitError):
    """The running Steam client does not support the interface versions of this SDK."""


class CallResultError(SteamError):
    """An asynchronous Steam API call failed. `reason` is the ESteamAPICallFailure code."""

    def __init__(self, reason: int, message: str | None = None) -> None:
        super().__init__(reason, message)  # for pickling, as in SteamInitError
        self.reason = reason
        self._message = message

    def __str__(self) -> str:
        return self._message or f"the Steam API call failed with reason {self.reason}"


class SteamWarning(UserWarning):
    """Something works but may misbehave, such as a steam_api library from another SDK version."""
