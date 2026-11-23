# Generated from Steamworks SDK 1.65 by tools/generator. Do not edit.
from collections.abc import Mapping
from typing import Final

SDK_VERSION: Final = "1.65"
# sha256 of the SDK's steam_api library, by its redistributable_bin folder.
LIBRARY_SHA256: Final[Mapping[str, str]] = {
    "linux64": "eb2dd015b84177cf4f4326fe578aab375fd8931bbbd719c7492420d9777007fe",
    "linuxarm64": "6010ff5049f0154a270092cb93729f1fc691d28e3b8a6f5fc6f8fcccfbd1e508",
    "osx": "a37faf19675b943a3c9717d25d9a881f5addb7f0ee728e03de7aac143ba759d2",
    "win64": "e6d9bafb9a41e42fba7b21553db49f8719027af3f0deb23ff86cfc44d60e776d",
}
# The interface versions init asks the Steam client to support, in the SDK's order.
INIT_INTERFACE_VERSIONS: Final[tuple[str, ...]] = (
    "SteamUtils011",
    "SteamNetworkingUtils004",
    "STEAMAPPS_INTERFACE_VERSION009",
    "SteamController008",
    "SteamFriends018",
    "STEAMHTMLSURFACE_INTERFACE_VERSION_005",
    "STEAMHTTP_INTERFACE_VERSION003",
    "SteamInput007",
    "STEAMINVENTORY_INTERFACE_V003",
    "SteamMatchMakingServers003",
    "SteamMatchMaking009",
    "STEAMMUSIC_INTERFACE_VERSION001",
    "SteamNetworkingMessages002",
    "SteamNetworkingSockets013",
    "SteamNetworking006",
    "STEAMPARENTALSETTINGS_INTERFACE_VERSION001",
    "SteamParties002",
    "STEAMREMOTEPLAY_INTERFACE_VERSION004",
    "STEAMREMOTESTORAGE_INTERFACE_VERSION016",
    "STEAMSCREENSHOTS_INTERFACE_VERSION003",
    "STEAMUGC_INTERFACE_VERSION021",
    "STEAMUSERSTATS_INTERFACE_VERSION013",
    "SteamUser023",
    "STEAMVIDEO_INTERFACE_V007",
)
