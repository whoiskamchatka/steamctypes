"""Value types shared across the API."""

import operator
from typing import NoReturn, Self

from steamctypes._generated.constants import (
    k_unSteamAccountIDMask,
    k_unSteamAccountInstanceMask,
    k_unSteamUserDefaultInstance,
)
from steamctypes._generated.enums import EAccountType, EUniverse

_MAX = (1 << 64) - 1


class SteamID:
    """A 64-bit Steam ID: account id, instance, account type and universe packed into one number."""

    __slots__ = ("_value",)
    _value: int

    def __init__(self, value: int) -> None:
        value = operator.index(value)
        if not 0 <= value <= _MAX:
            raise ValueError(f"a Steam ID is an unsigned 64-bit number, not {value}")
        object.__setattr__(self, "_value", value)

    def __setattr__(self, name: str, value: object) -> NoReturn:
        raise AttributeError("SteamID is immutable")

    def __delattr__(self, name: str) -> NoReturn:
        raise AttributeError("SteamID is immutable")

    # copy and pickle would otherwise restore the slot with setattr, which is blocked.
    def __reduce__(self) -> tuple[type[Self], tuple[int]]:
        return type(self), (self._value,)

    def __int__(self) -> int:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SteamID):
            return NotImplemented
        return self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return f"SteamID({self._value})"

    def __str__(self) -> str:
        return str(self._value)

    @property
    def account_id(self) -> int:
        return self._value & k_unSteamAccountIDMask

    @property
    def instance(self) -> int:
        return (self._value >> 32) & k_unSteamAccountInstanceMask

    @property
    def account_type(self) -> int:
        """An EAccountType value. Values outside the enum are kept as they are."""
        return (self._value >> 52) & 0xF

    @property
    def universe(self) -> int:
        """An EUniverse value. Values outside the enum are kept as they are."""
        return self._value >> 56

    @property
    def is_valid(self) -> bool:
        """The checks the SDK's CSteamID::IsValid makes."""
        account_type, account_id, instance = self.account_type, self.account_id, self.instance
        if not EAccountType.k_EAccountTypeInvalid < account_type < EAccountType.k_EAccountTypeMax:
            return False
        if not EUniverse.k_EUniverseInvalid < self.universe < EUniverse.k_EUniverseMax:
            return False
        if account_type == EAccountType.k_EAccountTypeIndividual:
            return account_id != 0 and instance == k_unSteamUserDefaultInstance
        if account_type == EAccountType.k_EAccountTypeClan:
            return account_id != 0 and instance == 0
        if account_type == EAccountType.k_EAccountTypeGameServer:
            return account_id != 0
        return True
