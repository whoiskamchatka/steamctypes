from steamctypes import SteamID


def test_steam_id_components() -> None:
    # Public universe (1), individual account (1), default instance (1), account id 12345.
    value = (1 << 56) | (1 << 52) | (1 << 32) | 12345
    steam_id = SteamID(value)

    assert (steam_id.account_id, steam_id.instance) == (12345, 1)
    assert (steam_id.account_type, steam_id.universe) == (1, 1)
    assert steam_id.is_valid
    assert int(steam_id) == value
    assert steam_id == SteamID(value)
    assert hash(steam_id) == hash(SteamID(value))
    assert repr(steam_id) == f"SteamID({value})"
    assert not SteamID(0).is_valid
