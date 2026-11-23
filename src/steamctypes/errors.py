"""Exceptions and warnings raised by steamctypes."""


class SteamError(Exception):
    """Base class of every steamctypes error."""


class LibraryNotFoundError(SteamError):
    """The steam_api library was not found."""


class IncompatibleLibraryError(SteamError):
    """The steam_api library cannot be used with this version of steamctypes."""


class SteamWarning(UserWarning):
    """Something works but may misbehave, such as a steam_api library from another SDK version."""
