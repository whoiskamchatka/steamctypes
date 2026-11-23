# Generated from Steamworks SDK 1.65 by tools/generator. Do not edit.
import ctypes
import sys

from . import typedefs

# Steam packs most structs to 8 bytes on Windows and 4 elsewhere. _layout_ 'ms' makes
# ctypes honour _pack_ the same way on every OS.
_PLATFORM_PACK = 8 if sys.platform == "win32" else 4


class SteamIPAddress_t_union(ctypes.Union):
    _pack_ = 1
    _layout_ = "ms"


class SteamIPAddress_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"
    _anonymous_ = ("_union",)


class FriendGameInfo_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class MatchMakingKeyValuePair_t(ctypes.Structure):
    pass


class servernetadr_t(ctypes.Structure):
    pass


class gameserveritem_t(ctypes.Structure):
    pass


class SteamPartyBeaconLocation_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamParamStringArray_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class LeaderboardEntry_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class P2PSessionState_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class InputAnalogActionData_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class InputDigitalActionData_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class InputMotionData_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class SteamInputActionEvent_t_union(ctypes.Union):
    _pack_ = 1
    _layout_ = "ms"


class SteamInputActionEvent_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"
    _anonymous_ = ("_union",)


class SteamUGCDetails_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamItemDetails_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class RemotePlayInputMouseMotion_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class RemotePlayInputMouseWheel_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class RemotePlayInputKey_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class RemotePlayInput_t_union(ctypes.Union):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class RemotePlayInput_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    _anonymous_ = ("_union",)


class SteamNetworkingIPAddr_union(ctypes.Union):
    _pack_ = 1
    _layout_ = "ms"


class SteamNetworkingIPAddr(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"
    _anonymous_ = ("_union",)


class SteamNetworkingIdentity_union(ctypes.Union):
    _pack_ = 1
    _layout_ = "ms"


class SteamNetworkingIdentity(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"
    _anonymous_ = ("_union",)


class SteamNetConnectionInfo_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamNetConnectionRealTimeStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamNetConnectionRealTimeLaneStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamNetworkingMessage_t(ctypes.Structure):
    pass


class SteamNetworkPingLocation_t(ctypes.Structure):
    pass


class SteamNetworkingConfigValue_t_m_val(ctypes.Union):
    pass


class SteamNetworkingConfigValue_t(ctypes.Structure):
    pass


class SteamDatagramHostedAddress(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamDatagramGameCoordinatorServerLogin(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"


class SteamServersConnected_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 101


class SteamServerConnectFailure_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 102


class SteamServersDisconnected_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 103


class ClientGameServerDeny_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 113


class IPCFailure_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 117


class LicensesUpdated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 125


class ValidateAuthTicketResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 143


class MicroTxnAuthorizationResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 152


class EncryptedAppTicketResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 154


class GetAuthSessionTicketResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 163


class GameWebCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 164


class StoreAuthURLResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 165


class MarketEligibilityResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 166


class DurationControl_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 167


class GetTicketForWebApiResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 168


class PersonaStateChange_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 304


class GameOverlayActivated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 331


class GameServerChangeRequested_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 332


class GameLobbyJoinRequested_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 333


class AvatarImageLoaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 334


class ClanOfficerListResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 335


class FriendRichPresenceUpdate_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 336


class GameRichPresenceJoinRequested_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 337


class GameConnectedClanChatMsg_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 338


class GameConnectedChatJoin_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 339


class GameConnectedChatLeave_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 340


class DownloadClanActivityCountsResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 341


class JoinClanChatRoomCompletionResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 342


class GameConnectedFriendChatMsg_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 343


class FriendsGetFollowerCount_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 344


class FriendsIsFollowing_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 345


class FriendsEnumerateFollowingList_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 346


class UnreadChatMessagesChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 348


class OverlayBrowserProtocolNavigation_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 349


class EquippedProfileItemsChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 350


class EquippedProfileItems_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 351


class IPCountry_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 701


class LowBatteryPower_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 702


class SteamAPICallCompleted_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 703


class SteamShutdown_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 704


class CheckFileSignature_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 705


class GamepadTextInputDismissed_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 714


class AppResumingFromSuspend_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 736


class FloatingGamepadTextInputDismissed_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 738


class FilterTextDictionaryChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 739


class FavoritesListChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 502


class LobbyInvite_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 503


class LobbyEnter_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 504


class LobbyDataUpdate_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 505


class LobbyChatUpdate_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 506


class LobbyChatMsg_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 507


class LobbyGameCreated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 509


class LobbyMatchList_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 510


class LobbyKicked_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 512


class LobbyCreated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 513


class FavoritesListAccountsUpdated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 516


class JoinPartyCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5301


class CreateBeaconCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5302


class ReservationNotificationCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5303


class ChangeNumOpenSlotsCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5304


class AvailableBeaconLocationsUpdated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5305


class ActiveBeaconsUpdated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5306


class RemoteStorageFileShareResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1307


class RemoteStoragePublishFileResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1309


class RemoteStorageDeletePublishedFileResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1311


class RemoteStorageEnumerateUserPublishedFilesResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1312


class RemoteStorageSubscribePublishedFileResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1313


class RemoteStorageEnumerateUserSubscribedFilesResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1314


class RemoteStorageUnsubscribePublishedFileResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1315


class RemoteStorageUpdatePublishedFileResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1316


class RemoteStorageDownloadUGCResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1317


class RemoteStorageGetPublishedFileDetailsResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1318


class RemoteStorageEnumerateWorkshopFilesResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1319


class RemoteStorageGetPublishedItemVoteDetailsResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1320


class RemoteStoragePublishedFileSubscribed_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1321


class RemoteStoragePublishedFileUnsubscribed_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1322


class RemoteStoragePublishedFileDeleted_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1323


class RemoteStorageUpdateUserPublishedItemVoteResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1324


class RemoteStorageUserVoteDetails_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1325


class RemoteStorageEnumerateUserSharedWorkshopFilesResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1326


class RemoteStorageSetUserPublishedFileActionResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1327


class RemoteStorageEnumeratePublishedFilesByUserActionResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1328


class RemoteStoragePublishFileProgress_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1329


class RemoteStoragePublishedFileUpdated_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1330


class RemoteStorageFileWriteAsyncComplete_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1331


class RemoteStorageFileReadAsyncComplete_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1332


class RemoteStorageLocalFileChange_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1333


class UserStatsReceived_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1101


class UserStatsStored_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1102


class UserAchievementStored_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1103


class LeaderboardFindResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1104


class LeaderboardScoresDownloaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1105


class LeaderboardScoreUploaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1106


class NumberOfCurrentPlayers_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1107


class UserStatsUnloaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1108


class UserAchievementIconFetched_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1109


class GlobalAchievementPercentagesReady_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1110


class LeaderboardUGCSet_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1111


class GlobalStatsReceived_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1112


class DlcInstalled_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1005


class NewUrlLaunchParameters_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1014


class AppProofOfPurchaseKeyResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1021


class FileDetailsResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1023


class TimedTrialStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1030


class P2PSessionRequest_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1202


class P2PSessionConnectFail_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1203


class SocketStatusCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1201


class ScreenshotReady_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2301


class ScreenshotRequested_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2302


class PlaybackStatusHasChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4001


class VolumeHasChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4002


class HTTPRequestCompleted_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2101


class HTTPRequestHeadersReceived_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2102


class HTTPRequestDataReceived_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2103


class SteamInputDeviceConnected_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2801


class SteamInputDeviceDisconnected_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2802


class SteamInputConfigurationLoaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2803


class SteamInputGamepadSlotChange_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 2804


class SteamUGCQueryCompleted_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3401


class SteamUGCRequestUGCDetailsResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3402


class CreateItemResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3403


class SubmitItemUpdateResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3404


class ItemInstalled_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3405


class DownloadItemResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3406


class UserFavoriteItemsListChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3407


class SetUserItemVoteResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3408


class GetUserItemVoteResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3409


class StartPlaytimeTrackingResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3410


class StopPlaytimeTrackingResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3411


class AddUGCDependencyResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3412


class RemoveUGCDependencyResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3413


class AddAppDependencyResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3414


class RemoveAppDependencyResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3415


class GetAppDependenciesResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3416


class DeleteItemResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3417


class UserSubscribedItemsListChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3418


class WorkshopEULAStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 3420


class HTML_BrowserReady_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4501


class HTML_NeedsPaint_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4502


class HTML_StartRequest_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4503


class HTML_CloseBrowser_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4504


class HTML_URLChanged_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4505


class HTML_FinishedRequest_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4506


class HTML_OpenLinkInNewTab_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4507


class HTML_ChangedTitle_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4508


class HTML_SearchResults_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4509


class HTML_CanGoBackAndForward_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4510


class HTML_HorizontalScroll_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4511


class HTML_VerticalScroll_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4512


class HTML_LinkAtPosition_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4513


class HTML_JSAlert_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4514


class HTML_JSConfirm_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4515


class HTML_FileOpenDialog_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4516


class HTML_NewWindow_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4521


class HTML_SetCursor_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4522


class HTML_StatusText_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4523


class HTML_ShowToolTip_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4524


class HTML_UpdateToolTip_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4525


class HTML_HideToolTip_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4526


class HTML_BrowserRestarted_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4527


class SteamInventoryResultReady_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4700


class SteamInventoryFullUpdate_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4701


class SteamInventoryDefinitionUpdate_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4702


class SteamInventoryEligiblePromoItemDefIDs_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4703


class SteamInventoryStartPurchaseResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4704


class SteamInventoryRequestPricesResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4705


class SteamTimelineGamePhaseRecordingExists_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 6001


class SteamTimelineEventRecordingExists_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 6002


class GetVideoURLResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4611


class GetOPFSettingsResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4624


class BroadcastUploadStart_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4604


class BroadcastUploadStop_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 4605


class SteamParentalSettingsChanged_t(ctypes.Structure):
    k_iCallback = 5001


class SteamRemotePlaySessionConnected_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5701


class SteamRemotePlaySessionDisconnected_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5702


class SteamRemotePlayTogetherGuestInvite_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5703


class SteamRemotePlaySessionAvatarLoaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 5704


class SteamNetworkingMessagesSessionRequest_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"
    k_iCallback = 1251


class SteamNetworkingMessagesSessionFailed_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"
    k_iCallback = 1252


class SteamNetConnectionStatusChangedCallback_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1221


class SteamNetAuthenticationStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1222


class SteamRelayNetworkStatus_t(ctypes.Structure):
    k_iCallback = 1281


class GSClientApprove_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 201


class GSClientDeny_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 202


class GSClientKick_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 203


class GSClientAchievementStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 206


class GSPolicyResponse_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 115


class GSGameplayStats_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 207


class GSClientGroupStatus_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 208


class GSReputation_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 209


class AssociateWithClanResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 210


class ComputeNewPlayerCompatibilityResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 211


class GSStatsReceived_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1800


class GSStatsStored_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1801


class GSStatsUnloaded_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1108


class SteamNetworkingFakeIPResult_t(ctypes.Structure):
    _pack_ = _PLATFORM_PACK
    _layout_ = "ms"
    k_iCallback = 1223


class CSteamID(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class CGameID(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class SteamInputActionEvent_t_AnalogAction_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class SteamInputActionEvent_t_DigitalAction_t(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


class SteamNetworkingIPAddr_IPv4MappedAddress(ctypes.Structure):
    _pack_ = 1
    _layout_ = "ms"


SteamIPAddress_t_union._fields_ = [
    ("m_unIPv4", typedefs.uint32),
    ("m_rgubIPv6", typedefs.uint8 * 16),
    ("m_ipv6Qword", typedefs.uint64 * 2),
]
SteamIPAddress_t._fields_ = [("_union", SteamIPAddress_t_union), ("m_eType", ctypes.c_int)]
CGameID._fields_ = [("m_ulGameID", typedefs.uint64)]
CSteamID._fields_ = [("m_steamid", typedefs.uint64)]
FriendGameInfo_t._fields_ = [
    ("m_gameID", CGameID),
    ("m_unGameIP", typedefs.uint32),
    ("m_usGamePort", typedefs.uint16),
    ("m_usQueryPort", typedefs.uint16),
    ("m_steamIDLobby", CSteamID),
]
MatchMakingKeyValuePair_t._fields_ = [
    ("m_szKey", ctypes.c_char * 256),
    ("m_szValue", ctypes.c_char * 256),
]
servernetadr_t._fields_ = [
    ("m_usConnectionPort", typedefs.uint16),
    ("m_usQueryPort", typedefs.uint16),
    ("m_unIP", typedefs.uint32),
]
gameserveritem_t._fields_ = [
    ("m_NetAdr", servernetadr_t),
    ("m_nPing", ctypes.c_int),
    ("m_bHadSuccessfulResponse", ctypes.c_bool),
    ("m_bDoNotRefresh", ctypes.c_bool),
    ("m_szGameDir", ctypes.c_char * 32),
    ("m_szMap", ctypes.c_char * 32),
    ("m_szGameDescription", ctypes.c_char * 64),
    ("m_nAppID", typedefs.uint32),
    ("m_nPlayers", ctypes.c_int),
    ("m_nMaxPlayers", ctypes.c_int),
    ("m_nBotPlayers", ctypes.c_int),
    ("m_bPassword", ctypes.c_bool),
    ("m_bSecure", ctypes.c_bool),
    ("m_ulTimeLastPlayed", typedefs.uint32),
    ("m_nServerVersion", ctypes.c_int),
    ("m_szServerName", ctypes.c_char * 64),
    ("m_szGameTags", ctypes.c_char * 128),
    ("m_steamID", CSteamID),
    ("m_nCurrentFriendCount", ctypes.c_int),
    ("m_nTotalFriendCount", ctypes.c_int),
]
SteamPartyBeaconLocation_t._fields_ = [
    ("m_eType", ctypes.c_int),
    ("m_ulLocationID", typedefs.uint64),
]
SteamParamStringArray_t._fields_ = [
    ("m_ppStrings", ctypes.POINTER(ctypes.c_char_p)),
    ("m_nNumStrings", typedefs.int32),
]
LeaderboardEntry_t._fields_ = [
    ("m_steamIDUser", CSteamID),
    ("m_nGlobalRank", typedefs.int32),
    ("m_nScore", typedefs.int32),
    ("m_cDetails", typedefs.int32),
    ("m_hUGC", typedefs.UGCHandle_t),
]
P2PSessionState_t._fields_ = [
    ("m_bConnectionActive", typedefs.uint8),
    ("m_bConnecting", typedefs.uint8),
    ("m_eP2PSessionError", typedefs.uint8),
    ("m_bUsingRelay", typedefs.uint8),
    ("m_nBytesQueuedForSend", typedefs.int32),
    ("m_nPacketsQueuedForSend", typedefs.int32),
    ("m_nRemoteIP", typedefs.uint32),
    ("m_nRemotePort", typedefs.uint16),
]
InputAnalogActionData_t._fields_ = [
    ("eMode", ctypes.c_int),
    ("x", ctypes.c_float),
    ("y", ctypes.c_float),
    ("bActive", ctypes.c_bool),
]
InputDigitalActionData_t._fields_ = [("bState", ctypes.c_bool), ("bActive", ctypes.c_bool)]
InputMotionData_t._fields_ = [
    ("rotQuatX", ctypes.c_float),
    ("rotQuatY", ctypes.c_float),
    ("rotQuatZ", ctypes.c_float),
    ("rotQuatW", ctypes.c_float),
    ("posAccelX", ctypes.c_float),
    ("posAccelY", ctypes.c_float),
    ("posAccelZ", ctypes.c_float),
    ("rotVelX", ctypes.c_float),
    ("rotVelY", ctypes.c_float),
    ("rotVelZ", ctypes.c_float),
]
SteamInputActionEvent_t_AnalogAction_t._fields_ = [
    ("actionHandle", typedefs.InputAnalogActionHandle_t),
    ("analogActionData", InputAnalogActionData_t),
]
SteamInputActionEvent_t_DigitalAction_t._fields_ = [
    ("actionHandle", typedefs.InputDigitalActionHandle_t),
    ("digitalActionData", InputDigitalActionData_t),
]
SteamInputActionEvent_t_union._fields_ = [
    ("analogAction", SteamInputActionEvent_t_AnalogAction_t),
    ("digitalAction", SteamInputActionEvent_t_DigitalAction_t),
]
SteamInputActionEvent_t._fields_ = [
    ("controllerHandle", typedefs.InputHandle_t),
    ("eEventType", ctypes.c_int),
    ("_union", SteamInputActionEvent_t_union),
]
SteamUGCDetails_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eResult", ctypes.c_int),
    ("m_eFileType", ctypes.c_int),
    ("m_nCreatorAppID", typedefs.AppId_t),
    ("m_nConsumerAppID", typedefs.AppId_t),
    ("m_rgchTitle", ctypes.c_char * 129),
    ("m_rgchDescription", ctypes.c_char * 8000),
    ("m_ulSteamIDOwner", typedefs.uint64),
    ("m_rtimeCreated", typedefs.uint32),
    ("m_rtimeUpdated", typedefs.uint32),
    ("m_rtimeAddedToUserList", typedefs.uint32),
    ("m_eVisibility", ctypes.c_int),
    ("m_bBanned", ctypes.c_bool),
    ("m_bAcceptedForUse", ctypes.c_bool),
    ("m_bTagsTruncated", ctypes.c_bool),
    ("m_rgchTags", ctypes.c_char * 1025),
    ("m_hFile", typedefs.UGCHandle_t),
    ("m_hPreviewFile", typedefs.UGCHandle_t),
    ("m_pchFileName", ctypes.c_char * 260),
    ("m_nFileSize", typedefs.int32),
    ("m_nPreviewFileSize", typedefs.int32),
    ("m_rgchURL", ctypes.c_char * 256),
    ("m_unVotesUp", typedefs.uint32),
    ("m_unVotesDown", typedefs.uint32),
    ("m_flScore", ctypes.c_float),
    ("m_unNumChildren", typedefs.uint32),
    ("m_ulTotalFilesSize", typedefs.uint64),
]
SteamItemDetails_t._fields_ = [
    ("m_itemId", typedefs.SteamItemInstanceID_t),
    ("m_iDefinition", typedefs.SteamItemDef_t),
    ("m_unQuantity", typedefs.uint16),
    ("m_unFlags", typedefs.uint16),
]
RemotePlayInputMouseMotion_t._fields_ = [
    ("m_bAbsolute", ctypes.c_bool),
    ("m_flNormalizedX", ctypes.c_float),
    ("m_flNormalizedY", ctypes.c_float),
    ("m_nDeltaX", ctypes.c_int),
    ("m_nDeltaY", ctypes.c_int),
]
RemotePlayInputMouseWheel_t._fields_ = [
    ("m_eDirection", ctypes.c_int),
    ("m_flAmount", ctypes.c_float),
]
RemotePlayInputKey_t._fields_ = [
    ("m_eScancode", ctypes.c_int),
    ("m_unModifiers", typedefs.uint32),
    ("m_unKeycode", typedefs.uint32),
]
RemotePlayInput_t_union._fields_ = [
    ("m_MouseMotion", RemotePlayInputMouseMotion_t),
    ("m_eMouseButton", ctypes.c_int),
    ("m_MouseWheel", RemotePlayInputMouseWheel_t),
    ("m_Key", RemotePlayInputKey_t),
    ("padding", ctypes.c_char * 56),
]
RemotePlayInput_t._fields_ = [
    ("m_unSessionID", typedefs.RemotePlaySessionID_t),
    ("m_eType", ctypes.c_int),
    ("_union", RemotePlayInput_t_union),
]
SteamNetworkingIPAddr_IPv4MappedAddress._fields_ = [
    ("m_8zeros", typedefs.uint64),
    ("m_0000", typedefs.uint16),
    ("m_ffff", typedefs.uint16),
    ("m_ip", typedefs.uint8 * 4),
]
SteamNetworkingIPAddr_union._fields_ = [
    ("m_ipv6", typedefs.uint8 * 16),
    ("m_ipv4", SteamNetworkingIPAddr_IPv4MappedAddress),
]
SteamNetworkingIPAddr._fields_ = [
    ("_union", SteamNetworkingIPAddr_union),
    ("m_port", typedefs.uint16),
]
SteamNetworkingIdentity_union._fields_ = [
    ("m_steamID64", typedefs.uint64),
    ("m_PSNID", typedefs.uint64),
    ("m_szGenericString", ctypes.c_char * 32),
    ("m_szXboxPairwiseID", ctypes.c_char * 33),
    ("m_genericBytes", typedefs.uint8 * 32),
    ("m_szUnknownRawString", ctypes.c_char * 128),
    ("m_ip", SteamNetworkingIPAddr),
    ("m_reserved", typedefs.uint32 * 32),
]
SteamNetworkingIdentity._fields_ = [
    ("m_eType", ctypes.c_int),
    ("m_cbSize", ctypes.c_int),
    ("_union", SteamNetworkingIdentity_union),
]
SteamNetConnectionInfo_t._fields_ = [
    ("m_identityRemote", SteamNetworkingIdentity),
    ("m_nUserData", typedefs.int64),
    ("m_hListenSocket", typedefs.HSteamListenSocket),
    ("m_addrRemote", SteamNetworkingIPAddr),
    ("m__pad1", typedefs.uint16),
    ("m_idPOPRemote", typedefs.SteamNetworkingPOPID),
    ("m_idPOPRelay", typedefs.SteamNetworkingPOPID),
    ("m_eState", ctypes.c_int),
    ("m_eEndReason", ctypes.c_int),
    ("m_szEndDebug", ctypes.c_char * 128),
    ("m_szConnectionDescription", ctypes.c_char * 128),
    ("m_nFlags", ctypes.c_int),
    ("reserved", typedefs.uint32 * 63),
]
SteamNetConnectionRealTimeStatus_t._fields_ = [
    ("m_eState", ctypes.c_int),
    ("m_nPing", ctypes.c_int),
    ("m_flConnectionQualityLocal", ctypes.c_float),
    ("m_flConnectionQualityRemote", ctypes.c_float),
    ("m_flOutPacketsPerSec", ctypes.c_float),
    ("m_flOutBytesPerSec", ctypes.c_float),
    ("m_flInPacketsPerSec", ctypes.c_float),
    ("m_flInBytesPerSec", ctypes.c_float),
    ("m_nSendRateBytesPerSecond", ctypes.c_int),
    ("m_cbPendingUnreliable", ctypes.c_int),
    ("m_cbPendingReliable", ctypes.c_int),
    ("m_cbSentUnackedReliable", ctypes.c_int),
    ("m_usecQueueTime", typedefs.SteamNetworkingMicroseconds),
    ("m_usecMaxJitter", typedefs.int32),
    ("reserved", typedefs.uint32 * 15),
]
SteamNetConnectionRealTimeLaneStatus_t._fields_ = [
    ("m_cbPendingUnreliable", ctypes.c_int),
    ("m_cbPendingReliable", ctypes.c_int),
    ("m_cbSentUnackedReliable", ctypes.c_int),
    ("_reservePad1", ctypes.c_int),
    ("m_usecQueueTime", typedefs.SteamNetworkingMicroseconds),
    ("reserved", typedefs.uint32 * 10),
]
SteamNetworkingMessage_t._fields_ = [
    ("m_pData", ctypes.c_void_p),
    ("m_cbSize", ctypes.c_int),
    ("m_conn", typedefs.HSteamNetConnection),
    ("m_identityPeer", SteamNetworkingIdentity),
    ("m_nConnUserData", typedefs.int64),
    ("m_usecTimeReceived", typedefs.SteamNetworkingMicroseconds),
    ("m_nMessageNumber", typedefs.int64),
    ("m_pfnFreeData", ctypes.c_void_p),
    ("m_pfnRelease", ctypes.c_void_p),
    ("m_nChannel", ctypes.c_int),
    ("m_nFlags", ctypes.c_int),
    ("m_nUserData", typedefs.int64),
    ("m_idxLane", typedefs.uint16),
    ("_pad1__", typedefs.uint16),
]
SteamNetworkPingLocation_t._fields_ = [("m_data", typedefs.uint8 * 512)]
SteamNetworkingConfigValue_t_m_val._fields_ = [
    ("m_int32", ctypes.c_int32),
    ("m_int64", ctypes.c_int64),
    ("m_float", ctypes.c_float),
    ("m_string", ctypes.c_char_p),
    ("m_ptr", ctypes.c_void_p),
]
SteamNetworkingConfigValue_t._fields_ = [
    ("m_eValue", ctypes.c_int),
    ("m_eDataType", ctypes.c_int),
    ("m_val", SteamNetworkingConfigValue_t_m_val),
]
SteamDatagramHostedAddress._fields_ = [("m_cbSize", ctypes.c_int), ("m_data", ctypes.c_char * 128)]
SteamDatagramGameCoordinatorServerLogin._fields_ = [
    ("m_identity", SteamNetworkingIdentity),
    ("m_routing", SteamDatagramHostedAddress),
    ("m_nAppID", typedefs.AppId_t),
    ("m_rtime", typedefs.RTime32),
    ("m_cbAppData", ctypes.c_int),
    ("m_appData", ctypes.c_char * 2048),
]
SteamServersConnected_t._fields_ = [("_padding", ctypes.c_ubyte)]
SteamServerConnectFailure_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_bStillRetrying", ctypes.c_bool),
]
SteamServersDisconnected_t._fields_ = [("m_eResult", ctypes.c_int)]
ClientGameServerDeny_t._fields_ = [
    ("m_uAppID", typedefs.uint32),
    ("m_unGameServerIP", typedefs.uint32),
    ("m_usGameServerPort", typedefs.uint16),
    ("m_bSecure", typedefs.uint16),
    ("m_uReason", typedefs.uint32),
]
IPCFailure_t._fields_ = [("m_eFailureType", typedefs.uint8)]
LicensesUpdated_t._fields_ = [("_padding", ctypes.c_ubyte)]
ValidateAuthTicketResponse_t._fields_ = [
    ("m_SteamID", CSteamID),
    ("m_eAuthSessionResponse", ctypes.c_int),
    ("m_OwnerSteamID", CSteamID),
]
MicroTxnAuthorizationResponse_t._fields_ = [
    ("m_unAppID", typedefs.uint32),
    ("m_ulOrderID", typedefs.uint64),
    ("m_bAuthorized", typedefs.uint8),
]
EncryptedAppTicketResponse_t._fields_ = [("m_eResult", ctypes.c_int)]
GetAuthSessionTicketResponse_t._fields_ = [
    ("m_hAuthTicket", typedefs.HAuthTicket),
    ("m_eResult", ctypes.c_int),
]
GameWebCallback_t._fields_ = [("m_szURL", ctypes.c_char * 256)]
StoreAuthURLResponse_t._fields_ = [("m_szURL", ctypes.c_char * 512)]
MarketEligibilityResponse_t._fields_ = [
    ("m_bAllowed", ctypes.c_bool),
    ("m_eNotAllowedReason", ctypes.c_int),
    ("m_rtAllowedAtTime", typedefs.RTime32),
    ("m_cdaySteamGuardRequiredDays", ctypes.c_int),
    ("m_cdayNewDeviceCooldown", ctypes.c_int),
]
DurationControl_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_appid", typedefs.AppId_t),
    ("m_bApplicable", ctypes.c_bool),
    ("m_csecsLast5h", typedefs.int32),
    ("m_progress", ctypes.c_int),
    ("m_notification", ctypes.c_int),
    ("m_csecsToday", typedefs.int32),
    ("m_csecsRemaining", typedefs.int32),
]
GetTicketForWebApiResponse_t._fields_ = [
    ("m_hAuthTicket", typedefs.HAuthTicket),
    ("m_eResult", ctypes.c_int),
    ("m_cubTicket", ctypes.c_int),
    ("m_rgubTicket", typedefs.uint8 * 2560),
]
PersonaStateChange_t._fields_ = [("m_ulSteamID", typedefs.uint64), ("m_nChangeFlags", ctypes.c_int)]
GameOverlayActivated_t._fields_ = [
    ("m_bActive", typedefs.uint8),
    ("m_bUserInitiated", ctypes.c_bool),
    ("m_nAppID", typedefs.AppId_t),
    ("m_dwOverlayPID", typedefs.uint32),
]
GameServerChangeRequested_t._fields_ = [
    ("m_rgchServer", ctypes.c_char * 64),
    ("m_rgchPassword", ctypes.c_char * 64),
]
GameLobbyJoinRequested_t._fields_ = [("m_steamIDLobby", CSteamID), ("m_steamIDFriend", CSteamID)]
AvatarImageLoaded_t._fields_ = [
    ("m_steamID", CSteamID),
    ("m_iImage", ctypes.c_int),
    ("m_iWide", ctypes.c_int),
    ("m_iTall", ctypes.c_int),
]
ClanOfficerListResponse_t._fields_ = [
    ("m_steamIDClan", CSteamID),
    ("m_cOfficers", ctypes.c_int),
    ("m_bSuccess", typedefs.uint8),
]
FriendRichPresenceUpdate_t._fields_ = [
    ("m_steamIDFriend", CSteamID),
    ("m_nAppID", typedefs.AppId_t),
]
GameRichPresenceJoinRequested_t._fields_ = [
    ("m_steamIDFriend", CSteamID),
    ("m_rgchConnect", ctypes.c_char * 256),
]
GameConnectedClanChatMsg_t._fields_ = [
    ("m_steamIDClanChat", CSteamID),
    ("m_steamIDUser", CSteamID),
    ("m_iMessageID", ctypes.c_int),
]
GameConnectedChatJoin_t._fields_ = [("m_steamIDClanChat", CSteamID), ("m_steamIDUser", CSteamID)]
GameConnectedChatLeave_t._fields_ = [
    ("m_steamIDClanChat", CSteamID),
    ("m_steamIDUser", CSteamID),
    ("m_bKicked", ctypes.c_bool),
    ("m_bDropped", ctypes.c_bool),
]
DownloadClanActivityCountsResult_t._fields_ = [("m_bSuccess", ctypes.c_bool)]
JoinClanChatRoomCompletionResult_t._fields_ = [
    ("m_steamIDClanChat", CSteamID),
    ("m_eChatRoomEnterResponse", ctypes.c_int),
]
GameConnectedFriendChatMsg_t._fields_ = [
    ("m_steamIDUser", CSteamID),
    ("m_iMessageID", ctypes.c_int),
]
FriendsGetFollowerCount_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_steamID", CSteamID),
    ("m_nCount", ctypes.c_int),
]
FriendsIsFollowing_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_steamID", CSteamID),
    ("m_bIsFollowing", ctypes.c_bool),
]
FriendsEnumerateFollowingList_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_rgSteamID", CSteamID * 50),
    ("m_nResultsReturned", typedefs.int32),
    ("m_nTotalResultCount", typedefs.int32),
]
UnreadChatMessagesChanged_t._fields_ = [("_padding", ctypes.c_ubyte)]
OverlayBrowserProtocolNavigation_t._fields_ = [("rgchURI", ctypes.c_char * 1024)]
EquippedProfileItemsChanged_t._fields_ = [("m_steamID", CSteamID)]
EquippedProfileItems_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_steamID", CSteamID),
    ("m_bHasAnimatedAvatar", ctypes.c_bool),
    ("m_bHasAvatarFrame", ctypes.c_bool),
    ("m_bHasProfileModifier", ctypes.c_bool),
    ("m_bHasProfileBackground", ctypes.c_bool),
    ("m_bHasMiniProfileBackground", ctypes.c_bool),
    ("m_bFromCache", ctypes.c_bool),
]
IPCountry_t._fields_ = [("_padding", ctypes.c_ubyte)]
LowBatteryPower_t._fields_ = [("m_nMinutesBatteryLeft", typedefs.uint8)]
SteamAPICallCompleted_t._fields_ = [
    ("m_hAsyncCall", typedefs.SteamAPICall_t),
    ("m_iCallback", ctypes.c_int),
    ("m_cubParam", typedefs.uint32),
]
SteamShutdown_t._fields_ = [("_padding", ctypes.c_ubyte)]
CheckFileSignature_t._fields_ = [("m_eCheckFileSignature", ctypes.c_int)]
GamepadTextInputDismissed_t._fields_ = [
    ("m_bSubmitted", ctypes.c_bool),
    ("m_unSubmittedText", typedefs.uint32),
    ("m_unAppID", typedefs.AppId_t),
]
AppResumingFromSuspend_t._fields_ = [("_padding", ctypes.c_ubyte)]
FloatingGamepadTextInputDismissed_t._fields_ = [("_padding", ctypes.c_ubyte)]
FilterTextDictionaryChanged_t._fields_ = [("m_eLanguage", ctypes.c_int)]
FavoritesListChanged_t._fields_ = [
    ("m_nIP", typedefs.uint32),
    ("m_nQueryPort", typedefs.uint32),
    ("m_nConnPort", typedefs.uint32),
    ("m_nAppID", typedefs.uint32),
    ("m_nFlags", typedefs.uint32),
    ("m_bAdd", ctypes.c_bool),
    ("m_unAccountId", typedefs.AccountID_t),
]
LobbyInvite_t._fields_ = [
    ("m_ulSteamIDUser", typedefs.uint64),
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_ulGameID", typedefs.uint64),
]
LobbyEnter_t._fields_ = [
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_rgfChatPermissions", typedefs.uint32),
    ("m_bLocked", ctypes.c_bool),
    ("m_EChatRoomEnterResponse", typedefs.uint32),
]
LobbyDataUpdate_t._fields_ = [
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_ulSteamIDMember", typedefs.uint64),
    ("m_bSuccess", typedefs.uint8),
]
LobbyChatUpdate_t._fields_ = [
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_ulSteamIDUserChanged", typedefs.uint64),
    ("m_ulSteamIDMakingChange", typedefs.uint64),
    ("m_rgfChatMemberStateChange", typedefs.uint32),
]
LobbyChatMsg_t._fields_ = [
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_ulSteamIDUser", typedefs.uint64),
    ("m_eChatEntryType", typedefs.uint8),
    ("m_iChatID", typedefs.uint32),
]
LobbyGameCreated_t._fields_ = [
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_ulSteamIDGameServer", typedefs.uint64),
    ("m_unIP", typedefs.uint32),
    ("m_usPort", typedefs.uint16),
]
LobbyMatchList_t._fields_ = [("m_nLobbiesMatching", typedefs.uint32)]
LobbyKicked_t._fields_ = [
    ("m_ulSteamIDLobby", typedefs.uint64),
    ("m_ulSteamIDAdmin", typedefs.uint64),
    ("m_bKickedDueToDisconnect", typedefs.uint8),
]
LobbyCreated_t._fields_ = [("m_eResult", ctypes.c_int), ("m_ulSteamIDLobby", typedefs.uint64)]
FavoritesListAccountsUpdated_t._fields_ = [("m_eResult", ctypes.c_int)]
JoinPartyCallback_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_ulBeaconID", typedefs.PartyBeaconID_t),
    ("m_SteamIDBeaconOwner", CSteamID),
    ("m_rgchConnectString", ctypes.c_char * 256),
]
CreateBeaconCallback_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_ulBeaconID", typedefs.PartyBeaconID_t),
]
ReservationNotificationCallback_t._fields_ = [
    ("m_ulBeaconID", typedefs.PartyBeaconID_t),
    ("m_steamIDJoiner", CSteamID),
]
ChangeNumOpenSlotsCallback_t._fields_ = [("m_eResult", ctypes.c_int)]
AvailableBeaconLocationsUpdated_t._fields_ = [("_padding", ctypes.c_ubyte)]
ActiveBeaconsUpdated_t._fields_ = [("_padding", ctypes.c_ubyte)]
RemoteStorageFileShareResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_hFile", typedefs.UGCHandle_t),
    ("m_rgchFilename", ctypes.c_char * 260),
]
RemoteStoragePublishFileResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_bUserNeedsToAcceptWorkshopLegalAgreement", ctypes.c_bool),
]
RemoteStorageDeletePublishedFileResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
]
RemoteStorageEnumerateUserPublishedFilesResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nResultsReturned", typedefs.int32),
    ("m_nTotalResultCount", typedefs.int32),
    ("m_rgPublishedFileId", typedefs.PublishedFileId_t * 50),
]
RemoteStorageSubscribePublishedFileResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
]
RemoteStorageEnumerateUserSubscribedFilesResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nResultsReturned", typedefs.int32),
    ("m_nTotalResultCount", typedefs.int32),
    ("m_rgPublishedFileId", typedefs.PublishedFileId_t * 50),
    ("m_rgRTimeSubscribed", typedefs.uint32 * 50),
]
RemoteStorageUnsubscribePublishedFileResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
]
RemoteStorageUpdatePublishedFileResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_bUserNeedsToAcceptWorkshopLegalAgreement", ctypes.c_bool),
]
RemoteStorageDownloadUGCResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_hFile", typedefs.UGCHandle_t),
    ("m_nAppID", typedefs.AppId_t),
    ("m_nSizeInBytes", typedefs.int32),
    ("m_pchFileName", ctypes.c_char * 260),
    ("m_ulSteamIDOwner", typedefs.uint64),
]
RemoteStorageGetPublishedFileDetailsResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nCreatorAppID", typedefs.AppId_t),
    ("m_nConsumerAppID", typedefs.AppId_t),
    ("m_rgchTitle", ctypes.c_char * 129),
    ("m_rgchDescription", ctypes.c_char * 8000),
    ("m_hFile", typedefs.UGCHandle_t),
    ("m_hPreviewFile", typedefs.UGCHandle_t),
    ("m_ulSteamIDOwner", typedefs.uint64),
    ("m_rtimeCreated", typedefs.uint32),
    ("m_rtimeUpdated", typedefs.uint32),
    ("m_eVisibility", ctypes.c_int),
    ("m_bBanned", ctypes.c_bool),
    ("m_rgchTags", ctypes.c_char * 1025),
    ("m_bTagsTruncated", ctypes.c_bool),
    ("m_pchFileName", ctypes.c_char * 260),
    ("m_nFileSize", typedefs.int32),
    ("m_nPreviewFileSize", typedefs.int32),
    ("m_rgchURL", ctypes.c_char * 256),
    ("m_eFileType", ctypes.c_int),
    ("m_bAcceptedForUse", ctypes.c_bool),
]
RemoteStorageEnumerateWorkshopFilesResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nResultsReturned", typedefs.int32),
    ("m_nTotalResultCount", typedefs.int32),
    ("m_rgPublishedFileId", typedefs.PublishedFileId_t * 50),
    ("m_rgScore", ctypes.c_float * 50),
    ("m_nAppId", typedefs.AppId_t),
    ("m_unStartIndex", typedefs.uint32),
]
RemoteStorageGetPublishedItemVoteDetailsResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_unPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nVotesFor", typedefs.int32),
    ("m_nVotesAgainst", typedefs.int32),
    ("m_nReports", typedefs.int32),
    ("m_fScore", ctypes.c_float),
]
RemoteStoragePublishedFileSubscribed_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nAppID", typedefs.AppId_t),
]
RemoteStoragePublishedFileUnsubscribed_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nAppID", typedefs.AppId_t),
]
RemoteStoragePublishedFileDeleted_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nAppID", typedefs.AppId_t),
]
RemoteStorageUpdateUserPublishedItemVoteResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
]
RemoteStorageUserVoteDetails_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eVote", ctypes.c_int),
]
RemoteStorageEnumerateUserSharedWorkshopFilesResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nResultsReturned", typedefs.int32),
    ("m_nTotalResultCount", typedefs.int32),
    ("m_rgPublishedFileId", typedefs.PublishedFileId_t * 50),
]
RemoteStorageSetUserPublishedFileActionResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eAction", ctypes.c_int),
]
RemoteStorageEnumeratePublishedFilesByUserActionResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_eAction", ctypes.c_int),
    ("m_nResultsReturned", typedefs.int32),
    ("m_nTotalResultCount", typedefs.int32),
    ("m_rgPublishedFileId", typedefs.PublishedFileId_t * 50),
    ("m_rgRTimeUpdated", typedefs.uint32 * 50),
]
RemoteStoragePublishFileProgress_t._fields_ = [
    ("m_dPercentFile", ctypes.c_double),
    ("m_bPreview", ctypes.c_bool),
]
RemoteStoragePublishedFileUpdated_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nAppID", typedefs.AppId_t),
    ("m_ulUnused", typedefs.uint64),
]
RemoteStorageFileWriteAsyncComplete_t._fields_ = [("m_eResult", ctypes.c_int)]
RemoteStorageFileReadAsyncComplete_t._fields_ = [
    ("m_hFileReadAsync", typedefs.SteamAPICall_t),
    ("m_eResult", ctypes.c_int),
    ("m_nOffset", typedefs.uint32),
    ("m_cubRead", typedefs.uint32),
]
RemoteStorageLocalFileChange_t._fields_ = [("_padding", ctypes.c_ubyte)]
UserStatsReceived_t._fields_ = [
    ("m_nGameID", typedefs.uint64),
    ("m_eResult", ctypes.c_int),
    ("m_steamIDUser", CSteamID),
]
UserStatsStored_t._fields_ = [("m_nGameID", typedefs.uint64), ("m_eResult", ctypes.c_int)]
UserAchievementStored_t._fields_ = [
    ("m_nGameID", typedefs.uint64),
    ("m_bGroupAchievement", ctypes.c_bool),
    ("m_rgchAchievementName", ctypes.c_char * 128),
    ("m_nCurProgress", typedefs.uint32),
    ("m_nMaxProgress", typedefs.uint32),
]
LeaderboardFindResult_t._fields_ = [
    ("m_hSteamLeaderboard", typedefs.SteamLeaderboard_t),
    ("m_bLeaderboardFound", typedefs.uint8),
]
LeaderboardScoresDownloaded_t._fields_ = [
    ("m_hSteamLeaderboard", typedefs.SteamLeaderboard_t),
    ("m_hSteamLeaderboardEntries", typedefs.SteamLeaderboardEntries_t),
    ("m_cEntryCount", ctypes.c_int),
]
LeaderboardScoreUploaded_t._fields_ = [
    ("m_bSuccess", typedefs.uint8),
    ("m_hSteamLeaderboard", typedefs.SteamLeaderboard_t),
    ("m_nScore", typedefs.int32),
    ("m_bScoreChanged", typedefs.uint8),
    ("m_nGlobalRankNew", ctypes.c_int),
    ("m_nGlobalRankPrevious", ctypes.c_int),
]
NumberOfCurrentPlayers_t._fields_ = [("m_bSuccess", typedefs.uint8), ("m_cPlayers", typedefs.int32)]
UserStatsUnloaded_t._fields_ = [("m_steamIDUser", CSteamID)]
UserAchievementIconFetched_t._fields_ = [
    ("m_nGameID", CGameID),
    ("m_rgchAchievementName", ctypes.c_char * 128),
    ("m_bAchieved", ctypes.c_bool),
    ("m_nIconHandle", ctypes.c_int),
]
GlobalAchievementPercentagesReady_t._fields_ = [
    ("m_nGameID", typedefs.uint64),
    ("m_eResult", ctypes.c_int),
]
LeaderboardUGCSet_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_hSteamLeaderboard", typedefs.SteamLeaderboard_t),
]
GlobalStatsReceived_t._fields_ = [("m_nGameID", typedefs.uint64), ("m_eResult", ctypes.c_int)]
DlcInstalled_t._fields_ = [("m_nAppID", typedefs.AppId_t)]
NewUrlLaunchParameters_t._fields_ = [("_padding", ctypes.c_ubyte)]
AppProofOfPurchaseKeyResponse_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nAppID", typedefs.uint32),
    ("m_cchKeyLength", typedefs.uint32),
    ("m_rgchKey", ctypes.c_char * 240),
]
FileDetailsResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_ulFileSize", typedefs.uint64),
    ("m_FileSHA", typedefs.uint8 * 20),
    ("m_unFlags", typedefs.uint32),
]
TimedTrialStatus_t._fields_ = [
    ("m_unAppID", typedefs.AppId_t),
    ("m_bIsOffline", ctypes.c_bool),
    ("m_unSecondsAllowed", typedefs.uint32),
    ("m_unSecondsPlayed", typedefs.uint32),
]
P2PSessionRequest_t._fields_ = [("m_steamIDRemote", CSteamID)]
P2PSessionConnectFail_t._fields_ = [
    ("m_steamIDRemote", CSteamID),
    ("m_eP2PSessionError", typedefs.uint8),
]
SocketStatusCallback_t._fields_ = [
    ("m_hSocket", typedefs.SNetSocket_t),
    ("m_hListenSocket", typedefs.SNetListenSocket_t),
    ("m_steamIDRemote", CSteamID),
    ("m_eSNetSocketState", ctypes.c_int),
]
ScreenshotReady_t._fields_ = [("m_hLocal", typedefs.ScreenshotHandle), ("m_eResult", ctypes.c_int)]
ScreenshotRequested_t._fields_ = [("_padding", ctypes.c_ubyte)]
PlaybackStatusHasChanged_t._fields_ = [("_padding", ctypes.c_ubyte)]
VolumeHasChanged_t._fields_ = [("m_flNewVolume", ctypes.c_float)]
HTTPRequestCompleted_t._fields_ = [
    ("m_hRequest", typedefs.HTTPRequestHandle),
    ("m_ulContextValue", typedefs.uint64),
    ("m_bRequestSuccessful", ctypes.c_bool),
    ("m_eStatusCode", ctypes.c_int),
    ("m_unBodySize", typedefs.uint32),
]
HTTPRequestHeadersReceived_t._fields_ = [
    ("m_hRequest", typedefs.HTTPRequestHandle),
    ("m_ulContextValue", typedefs.uint64),
]
HTTPRequestDataReceived_t._fields_ = [
    ("m_hRequest", typedefs.HTTPRequestHandle),
    ("m_ulContextValue", typedefs.uint64),
    ("m_cOffset", typedefs.uint32),
    ("m_cBytesReceived", typedefs.uint32),
]
SteamInputDeviceConnected_t._fields_ = [("m_ulConnectedDeviceHandle", typedefs.InputHandle_t)]
SteamInputDeviceDisconnected_t._fields_ = [("m_ulDisconnectedDeviceHandle", typedefs.InputHandle_t)]
SteamInputConfigurationLoaded_t._fields_ = [
    ("m_unAppID", typedefs.AppId_t),
    ("m_ulDeviceHandle", typedefs.InputHandle_t),
    ("m_ulMappingCreator", CSteamID),
    ("m_unMajorRevision", typedefs.uint32),
    ("m_unMinorRevision", typedefs.uint32),
    ("m_bUsesSteamInputAPI", ctypes.c_bool),
    ("m_bUsesGamepadAPI", ctypes.c_bool),
]
SteamInputGamepadSlotChange_t._fields_ = [
    ("m_unAppID", typedefs.AppId_t),
    ("m_ulDeviceHandle", typedefs.InputHandle_t),
    ("m_eDeviceType", ctypes.c_int),
    ("m_nOldGamepadSlot", ctypes.c_int),
    ("m_nNewGamepadSlot", ctypes.c_int),
]
SteamUGCQueryCompleted_t._fields_ = [
    ("m_handle", typedefs.UGCQueryHandle_t),
    ("m_eResult", ctypes.c_int),
    ("m_unNumResultsReturned", typedefs.uint32),
    ("m_unTotalMatchingResults", typedefs.uint32),
    ("m_bCachedData", ctypes.c_bool),
    ("m_rgchNextCursor", ctypes.c_char * 256),
]
SteamUGCRequestUGCDetailsResult_t._fields_ = [
    ("m_details", SteamUGCDetails_t),
    ("m_bCachedData", ctypes.c_bool),
]
CreateItemResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_bUserNeedsToAcceptWorkshopLegalAgreement", ctypes.c_bool),
]
SubmitItemUpdateResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_bUserNeedsToAcceptWorkshopLegalAgreement", ctypes.c_bool),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
]
ItemInstalled_t._fields_ = [
    ("m_unAppID", typedefs.AppId_t),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_hLegacyContent", typedefs.UGCHandle_t),
    ("m_unManifestID", typedefs.uint64),
]
DownloadItemResult_t._fields_ = [
    ("m_unAppID", typedefs.AppId_t),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eResult", ctypes.c_int),
]
UserFavoriteItemsListChanged_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eResult", ctypes.c_int),
    ("m_bWasAddRequest", ctypes.c_bool),
]
SetUserItemVoteResult_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eResult", ctypes.c_int),
    ("m_bVoteUp", ctypes.c_bool),
]
GetUserItemVoteResult_t._fields_ = [
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_eResult", ctypes.c_int),
    ("m_bVotedUp", ctypes.c_bool),
    ("m_bVotedDown", ctypes.c_bool),
    ("m_bVoteSkipped", ctypes.c_bool),
]
StartPlaytimeTrackingResult_t._fields_ = [("m_eResult", ctypes.c_int)]
StopPlaytimeTrackingResult_t._fields_ = [("m_eResult", ctypes.c_int)]
AddUGCDependencyResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nChildPublishedFileId", typedefs.PublishedFileId_t),
]
RemoveUGCDependencyResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nChildPublishedFileId", typedefs.PublishedFileId_t),
]
AddAppDependencyResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nAppID", typedefs.AppId_t),
]
RemoveAppDependencyResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_nAppID", typedefs.AppId_t),
]
GetAppDependenciesResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
    ("m_rgAppIDs", typedefs.AppId_t * 32),
    ("m_nNumAppDependencies", typedefs.uint32),
    ("m_nTotalNumAppDependencies", typedefs.uint32),
]
DeleteItemResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nPublishedFileId", typedefs.PublishedFileId_t),
]
UserSubscribedItemsListChanged_t._fields_ = [("m_nAppID", typedefs.AppId_t)]
WorkshopEULAStatus_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nAppID", typedefs.AppId_t),
    ("m_unVersion", typedefs.uint32),
    ("m_rtAction", typedefs.RTime32),
    ("m_bAccepted", ctypes.c_bool),
    ("m_bNeedsAction", ctypes.c_bool),
]
HTML_BrowserReady_t._fields_ = [("unBrowserHandle", typedefs.HHTMLBrowser)]
HTML_NeedsPaint_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pBGRA", ctypes.c_char_p),
    ("unWide", typedefs.uint32),
    ("unTall", typedefs.uint32),
    ("unUpdateX", typedefs.uint32),
    ("unUpdateY", typedefs.uint32),
    ("unUpdateWide", typedefs.uint32),
    ("unUpdateTall", typedefs.uint32),
    ("unScrollX", typedefs.uint32),
    ("unScrollY", typedefs.uint32),
    ("flPageScale", ctypes.c_float),
    ("unPageSerial", typedefs.uint32),
]
HTML_StartRequest_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchURL", ctypes.c_char_p),
    ("pchTarget", ctypes.c_char_p),
    ("pchPostData", ctypes.c_char_p),
    ("bIsRedirect", ctypes.c_bool),
]
HTML_CloseBrowser_t._fields_ = [("unBrowserHandle", typedefs.HHTMLBrowser)]
HTML_URLChanged_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchURL", ctypes.c_char_p),
    ("pchPostData", ctypes.c_char_p),
    ("bIsRedirect", ctypes.c_bool),
    ("pchPageTitle", ctypes.c_char_p),
    ("bNewNavigation", ctypes.c_bool),
]
HTML_FinishedRequest_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchURL", ctypes.c_char_p),
    ("pchPageTitle", ctypes.c_char_p),
]
HTML_OpenLinkInNewTab_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchURL", ctypes.c_char_p),
]
HTML_ChangedTitle_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchTitle", ctypes.c_char_p),
]
HTML_SearchResults_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("unResults", typedefs.uint32),
    ("unCurrentMatch", typedefs.uint32),
]
HTML_CanGoBackAndForward_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("bCanGoBack", ctypes.c_bool),
    ("bCanGoForward", ctypes.c_bool),
]
HTML_HorizontalScroll_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("unScrollMax", typedefs.uint32),
    ("unScrollCurrent", typedefs.uint32),
    ("flPageScale", ctypes.c_float),
    ("bVisible", ctypes.c_bool),
    ("unPageSize", typedefs.uint32),
]
HTML_VerticalScroll_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("unScrollMax", typedefs.uint32),
    ("unScrollCurrent", typedefs.uint32),
    ("flPageScale", ctypes.c_float),
    ("bVisible", ctypes.c_bool),
    ("unPageSize", typedefs.uint32),
]
HTML_LinkAtPosition_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("x", typedefs.uint32),
    ("y", typedefs.uint32),
    ("pchURL", ctypes.c_char_p),
    ("bInput", ctypes.c_bool),
    ("bLiveLink", ctypes.c_bool),
]
HTML_JSAlert_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchMessage", ctypes.c_char_p),
]
HTML_JSConfirm_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchMessage", ctypes.c_char_p),
]
HTML_FileOpenDialog_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchTitle", ctypes.c_char_p),
    ("pchInitialFile", ctypes.c_char_p),
]
HTML_NewWindow_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchURL", ctypes.c_char_p),
    ("unX", typedefs.uint32),
    ("unY", typedefs.uint32),
    ("unWide", typedefs.uint32),
    ("unTall", typedefs.uint32),
    ("unNewWindow_BrowserHandle_IGNORE", typedefs.HHTMLBrowser),
]
HTML_SetCursor_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("eMouseCursor", typedefs.uint32),
]
HTML_StatusText_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchMsg", ctypes.c_char_p),
]
HTML_ShowToolTip_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchMsg", ctypes.c_char_p),
]
HTML_UpdateToolTip_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("pchMsg", ctypes.c_char_p),
]
HTML_HideToolTip_t._fields_ = [("unBrowserHandle", typedefs.HHTMLBrowser)]
HTML_BrowserRestarted_t._fields_ = [
    ("unBrowserHandle", typedefs.HHTMLBrowser),
    ("unOldBrowserHandle", typedefs.HHTMLBrowser),
]
SteamInventoryResultReady_t._fields_ = [
    ("m_handle", typedefs.SteamInventoryResult_t),
    ("m_result", ctypes.c_int),
]
SteamInventoryFullUpdate_t._fields_ = [("m_handle", typedefs.SteamInventoryResult_t)]
SteamInventoryDefinitionUpdate_t._fields_ = [("_padding", ctypes.c_ubyte)]
SteamInventoryEligiblePromoItemDefIDs_t._fields_ = [
    ("m_result", ctypes.c_int),
    ("m_steamID", CSteamID),
    ("m_numEligiblePromoItemDefs", ctypes.c_int),
    ("m_bCachedData", ctypes.c_bool),
]
SteamInventoryStartPurchaseResult_t._fields_ = [
    ("m_result", ctypes.c_int),
    ("m_ulOrderID", typedefs.uint64),
    ("m_ulTransID", typedefs.uint64),
]
SteamInventoryRequestPricesResult_t._fields_ = [
    ("m_result", ctypes.c_int),
    ("m_rgchCurrency", ctypes.c_char * 4),
]
SteamTimelineGamePhaseRecordingExists_t._fields_ = [
    ("m_rgchPhaseID", ctypes.c_char * 64),
    ("m_ulRecordingMS", typedefs.uint64),
    ("m_ulLongestClipMS", typedefs.uint64),
    ("m_unClipCount", typedefs.uint32),
    ("m_unScreenshotCount", typedefs.uint32),
]
SteamTimelineEventRecordingExists_t._fields_ = [
    ("m_ulEventID", typedefs.uint64),
    ("m_bRecordingExists", ctypes.c_bool),
]
GetVideoURLResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_unVideoAppID", typedefs.AppId_t),
    ("m_rgchURL", ctypes.c_char * 256),
]
GetOPFSettingsResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_unVideoAppID", typedefs.AppId_t),
]
BroadcastUploadStart_t._fields_ = [("m_bIsRTMP", ctypes.c_bool)]
BroadcastUploadStop_t._fields_ = [("m_eResult", ctypes.c_int)]
SteamParentalSettingsChanged_t._fields_ = [("_padding", ctypes.c_ubyte)]
SteamRemotePlaySessionConnected_t._fields_ = [("m_unSessionID", typedefs.RemotePlaySessionID_t)]
SteamRemotePlaySessionDisconnected_t._fields_ = [("m_unSessionID", typedefs.RemotePlaySessionID_t)]
SteamRemotePlayTogetherGuestInvite_t._fields_ = [("m_szConnectURL", ctypes.c_char * 1024)]
SteamRemotePlaySessionAvatarLoaded_t._fields_ = [
    ("m_unSessionID", typedefs.RemotePlaySessionID_t),
    ("m_iImage", ctypes.c_int),
    ("m_iWide", ctypes.c_int),
    ("m_iTall", ctypes.c_int),
]
SteamNetworkingMessagesSessionRequest_t._fields_ = [("m_identityRemote", SteamNetworkingIdentity)]
SteamNetworkingMessagesSessionFailed_t._fields_ = [("m_info", SteamNetConnectionInfo_t)]
SteamNetConnectionStatusChangedCallback_t._fields_ = [
    ("m_hConn", typedefs.HSteamNetConnection),
    ("m_info", SteamNetConnectionInfo_t),
    ("m_eOldState", ctypes.c_int),
]
SteamNetAuthenticationStatus_t._fields_ = [
    ("m_eAvail", ctypes.c_int),
    ("m_debugMsg", ctypes.c_char * 256),
]
SteamRelayNetworkStatus_t._fields_ = [
    ("m_eAvail", ctypes.c_int),
    ("m_bPingMeasurementInProgress", ctypes.c_int),
    ("m_eAvailNetworkConfig", ctypes.c_int),
    ("m_eAvailAnyRelay", ctypes.c_int),
    ("m_debugMsg", ctypes.c_char * 256),
]
GSClientApprove_t._fields_ = [("m_SteamID", CSteamID), ("m_OwnerSteamID", CSteamID)]
GSClientDeny_t._fields_ = [
    ("m_SteamID", CSteamID),
    ("m_eDenyReason", ctypes.c_int),
    ("m_rgchOptionalText", ctypes.c_char * 128),
]
GSClientKick_t._fields_ = [("m_SteamID", CSteamID), ("m_eDenyReason", ctypes.c_int)]
GSClientAchievementStatus_t._fields_ = [
    ("m_SteamID", typedefs.uint64),
    ("m_pchAchievement", ctypes.c_char * 128),
    ("m_bUnlocked", ctypes.c_bool),
]
GSPolicyResponse_t._fields_ = [("m_bSecure", typedefs.uint8)]
GSGameplayStats_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_nRank", typedefs.int32),
    ("m_unTotalConnects", typedefs.uint32),
    ("m_unTotalMinutesPlayed", typedefs.uint32),
]
GSClientGroupStatus_t._fields_ = [
    ("m_SteamIDUser", CSteamID),
    ("m_SteamIDGroup", CSteamID),
    ("m_bMember", ctypes.c_bool),
    ("m_bOfficer", ctypes.c_bool),
]
GSReputation_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_unReputationScore", typedefs.uint32),
    ("m_bBanned", ctypes.c_bool),
    ("m_unBannedIP", typedefs.uint32),
    ("m_usBannedPort", typedefs.uint16),
    ("m_ulBannedGameID", typedefs.uint64),
    ("m_unBanExpires", typedefs.uint32),
]
AssociateWithClanResult_t._fields_ = [("m_eResult", ctypes.c_int)]
ComputeNewPlayerCompatibilityResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_cPlayersThatDontLikeCandidate", ctypes.c_int),
    ("m_cPlayersThatCandidateDoesntLike", ctypes.c_int),
    ("m_cClanPlayersThatDontLikeCandidate", ctypes.c_int),
    ("m_SteamIDCandidate", CSteamID),
]
GSStatsReceived_t._fields_ = [("m_eResult", ctypes.c_int), ("m_steamIDUser", CSteamID)]
GSStatsStored_t._fields_ = [("m_eResult", ctypes.c_int), ("m_steamIDUser", CSteamID)]
GSStatsUnloaded_t._fields_ = [("m_steamIDUser", CSteamID)]
SteamNetworkingFakeIPResult_t._fields_ = [
    ("m_eResult", ctypes.c_int),
    ("m_identity", SteamNetworkingIdentity),
    ("m_unIP", typedefs.uint32),
    ("m_unPorts", typedefs.uint16 * 8),
]
