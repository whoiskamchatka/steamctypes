# Generated from Steamworks SDK 1.65 by tools/generator. Do not edit.
import ctypes
from collections.abc import Mapping
from typing import Any, Final

from . import structs, typedefs

# restype and argtypes of every flat function and interface accessor. Interface and
# struct methods take the object pointer as their first argument.
Prototype = tuple[type[Any] | None, tuple[type[Any], ...]]

PROTOTYPES: Final[Mapping[str, Prototype]] = {
    "SteamAPI_ISteamClient_CreateSteamPipe": (typedefs.HSteamPipe, (ctypes.c_void_p,)),
    "SteamAPI_ISteamClient_BReleaseSteamPipe": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamPipe),
    ),
    "SteamAPI_ISteamClient_ConnectToGlobalUser": (
        typedefs.HSteamUser,
        (ctypes.c_void_p, typedefs.HSteamPipe),
    ),
    "SteamAPI_ISteamClient_CreateLocalUser": (
        typedefs.HSteamUser,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.HSteamPipe), ctypes.c_int),
    ),
    "SteamAPI_ISteamClient_ReleaseUser": (
        None,
        (ctypes.c_void_p, typedefs.HSteamPipe, typedefs.HSteamUser),
    ),
    "SteamAPI_ISteamClient_GetISteamUser": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamGameServer": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_SetLocalIPBinding": (
        None,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamIPAddress_t), typedefs.uint16),
    ),
    "SteamAPI_ISteamClient_GetISteamFriends": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamUtils": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamMatchmaking": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamMatchmakingServers": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamGenericInterface": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamUserStats": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamGameServerStats": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamApps": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamNetworking": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamRemoteStorage": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamScreenshots": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetIPCCallCount": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamClient_SetWarningMessageHook": (
        None,
        (ctypes.c_void_p, typedefs.SteamAPIWarningMessageHook_t),
    ),
    "SteamAPI_ISteamClient_BShutdownIfAllPipesClosed": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamClient_GetISteamHTTP": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamController": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamUGC": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamMusic": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamHTMLSurface": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamInventory": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamVideo": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamParentalSettings": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamInput": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamParties": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamClient_GetISteamRemotePlay": (
        ctypes.c_void_p,
        (ctypes.c_void_p, typedefs.HSteamUser, typedefs.HSteamPipe, ctypes.c_char_p),
    ),
    "SteamAPI_SteamUser_v023": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamUser_GetHSteamUser": (typedefs.HSteamUser, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_BLoggedOn": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_GetSteamID": (typedefs.uint64_steamid, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_InitiateGameConnection_DEPRECATED": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_int,
            typedefs.uint64_steamid,
            typedefs.uint32,
            typedefs.uint16,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamUser_TerminateGameConnection_DEPRECATED": (
        None,
        (ctypes.c_void_p, typedefs.uint32, typedefs.uint16),
    ),
    "SteamAPI_ISteamUser_TrackAppUsageEvent": (
        None,
        (ctypes.c_void_p, typedefs.uint64_gameid, ctypes.c_int, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUser_GetUserDataFolder": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamUser_StartVoiceRecording": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_StopVoiceRecording": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_GetAvailableVoice": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUser_GetVoice": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_bool,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
            ctypes.c_bool,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUser_DecompressVoice": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUser_GetVoiceOptimalSampleRate": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_GetAuthSessionTicket": (
        typedefs.HAuthTicket,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(structs.SteamNetworkingIdentity),
        ),
    ),
    "SteamAPI_ISteamUser_GetAuthTicketForWebApi": (
        typedefs.HAuthTicket,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUser_BeginAuthSession": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamUser_EndAuthSession": (None, (ctypes.c_void_p, typedefs.uint64_steamid)),
    "SteamAPI_ISteamUser_CancelAuthTicket": (None, (ctypes.c_void_p, typedefs.HAuthTicket)),
    "SteamAPI_ISteamUser_UserHasLicenseForApp": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamUser_BIsBehindNAT": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_AdvertiseGame": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint32, typedefs.uint16),
    ),
    "SteamAPI_ISteamUser_RequestEncryptedAppTicket": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamUser_GetEncryptedAppTicket": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(typedefs.uint32)),
    ),
    "SteamAPI_ISteamUser_GetGameBadgeLevel": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUser_GetPlayerSteamLevel": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_RequestStoreAuthURL": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUser_BIsPhoneVerified": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_BIsTwoFactorEnabled": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_BIsPhoneIdentifying": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_BIsPhoneRequiringVerification": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_GetMarketEligibility": (typedefs.SteamAPICall_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_GetDurationControl": (typedefs.SteamAPICall_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUser_BSetDurationControlOnlineState": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_SteamFriends_v018": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamFriends_GetPersonaName": (ctypes.c_char_p, (ctypes.c_void_p,)),
    "SteamAPI_ISteamFriends_GetPersonaState": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamFriends_GetFriendCount": (ctypes.c_int, (ctypes.c_void_p, ctypes.c_int)),
    "SteamAPI_ISteamFriends_GetFriendByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetFriendRelationship": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendPersonaState": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendPersonaName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendGamePlayed": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.POINTER(structs.FriendGameInfo_t)),
    ),
    "SteamAPI_ISteamFriends_GetFriendPersonaNameHistory": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetFriendSteamLevel": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetPlayerNickname": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendsGroupCount": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamFriends_GetFriendsGroupIDByIndex": (
        typedefs.FriendsGroupID_t,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetFriendsGroupName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.FriendsGroupID_t),
    ),
    "SteamAPI_ISteamFriends_GetFriendsGroupMembersCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.FriendsGroupID_t),
    ),
    "SteamAPI_ISteamFriends_GetFriendsGroupMembersList": (
        None,
        (
            ctypes.c_void_p,
            typedefs.FriendsGroupID_t,
            ctypes.POINTER(structs.CSteamID),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamFriends_HasFriend": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetClanCount": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamFriends_GetClanByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetClanName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetClanTag": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetClanActivityCounts": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamFriends_DownloadClanActivityCounts": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.POINTER(structs.CSteamID), ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetFriendCountFromSource": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendFromSourceByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_IsUserInSource": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_SetInGameVoiceSpeaking": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_bool),
    ),
    "SteamAPI_ISteamFriends_ActivateGameOverlay": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamFriends_ActivateGameOverlayToUser": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_ActivateGameOverlayToWebPage": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_ActivateGameOverlayToStore": (
        None,
        (ctypes.c_void_p, typedefs.AppId_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_SetPlayedWith": (None, (ctypes.c_void_p, typedefs.uint64_steamid)),
    "SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialog": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetSmallFriendAvatar": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetMediumFriendAvatar": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetLargeFriendAvatar": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_RequestUserInformation": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_bool),
    ),
    "SteamAPI_ISteamFriends_RequestClanOfficerList": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetClanOwner": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetClanOfficerCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetClanOfficerByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_SetRichPresence": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_ClearRichPresence": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamFriends_GetFriendRichPresence": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_GetFriendRichPresenceKeyCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendRichPresenceKeyByIndex": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_RequestFriendRichPresence": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_InviteUserToGame": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_GetCoplayFriendCount": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamFriends_GetCoplayFriend": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetFriendCoplayTime": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetFriendCoplayGame": (
        typedefs.AppId_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_JoinClanChatRoom": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_LeaveClanChatRoom": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetClanChatMemberCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetChatMemberByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_SendClanChatMessage": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_GetClanChatMessage": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_int,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(structs.CSteamID),
        ),
    ),
    "SteamAPI_ISteamFriends_IsClanChatAdmin": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_IsClanChatWindowOpenInSteam": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_OpenClanChatWindowInSteam": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_CloseClanChatWindowInSteam": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_SetListenForFriendsMessages": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_bool),
    ),
    "SteamAPI_ISteamFriends_ReplyToFriendMessage": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_GetFriendMessage": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_int,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamFriends_GetFollowerCount": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_IsFollowing": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_EnumerateFollowingList": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamFriends_IsClanPublic": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_IsClanOfficialGameGroup": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_GetNumChatsWithUnreadPriorityMessages": (
        ctypes.c_int,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_RegisterProtocolInOverlayBrowser": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialogConnectString": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamFriends_RequestEquippedProfileItems": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamFriends_BHasEquippedProfileItem": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetProfileItemPropertyString": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamFriends_GetProfileItemPropertyUint": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_SteamUtils_v011": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerUtils_v011": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamUtils_GetSecondsSinceAppActive": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetSecondsSinceComputerActive": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetConnectedUniverse": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetServerRealTime": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetIPCountry": (ctypes.c_char_p, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetImageSize": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamUtils_GetImageRGBA": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(typedefs.uint8), ctypes.c_int),
    ),
    "SteamAPI_ISteamUtils_GetCurrentBatteryPower": (typedefs.uint8, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetAppID": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_SetOverlayNotificationPosition": (None, (ctypes.c_void_p, ctypes.c_int)),
    "SteamAPI_ISteamUtils_IsAPICallCompleted": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SteamAPICall_t, ctypes.POINTER(ctypes.c_bool)),
    ),
    "SteamAPI_ISteamUtils_GetAPICallFailureReason": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SteamAPICall_t),
    ),
    "SteamAPI_ISteamUtils_GetAPICallResult": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamAPICall_t,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_bool),
        ),
    ),
    "SteamAPI_ISteamUtils_GetIPCCallCount": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_SetWarningMessageHook": (
        None,
        (ctypes.c_void_p, typedefs.SteamAPIWarningMessageHook_t),
    ),
    "SteamAPI_ISteamUtils_IsOverlayEnabled": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_BOverlayNeedsPresent": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_CheckFileSignature": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUtils_ShowGamepadTextInput": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_char_p,
        ),
    ),
    "SteamAPI_ISteamUtils_GetEnteredGamepadTextLength": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetEnteredGamepadTextInput": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamUtils_GetSteamUILanguage": (ctypes.c_char_p, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_IsSteamRunningInVR": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_SetOverlayNotificationInset": (
        None,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamUtils_IsSteamInBigPictureMode": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_StartVRDashboard": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_IsVRHeadsetStreamingEnabled": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_SetVRHeadsetStreamingEnabled": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamUtils_IsSteamChinaLauncher": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_InitFilterText": (ctypes.c_bool, (ctypes.c_void_p, typedefs.uint32)),
    "SteamAPI_ISteamUtils_FilterText": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            typedefs.uint64_steamid,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUtils_GetIPv6ConnectivityState": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamUtils_ShowFloatingGamepadTextInput": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamUtils_SetGameLauncherMode": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamUtils_DismissFloatingGamepadTextInput": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_DismissGamepadTextInput": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_IsRunningOnSteamHardware": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_GetSteamHardwareDefaultConfig": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUtils_IsRunningUnderProton": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_SteamMatchmaking_v009": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamMatchmaking_GetFavoriteGameCount": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmaking_GetFavoriteGame": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.AppId_t),
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint16),
            ctypes.POINTER(typedefs.uint16),
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamMatchmaking_AddFavoriteGame": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            typedefs.uint32,
            typedefs.uint16,
            typedefs.uint16,
            typedefs.uint32,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamMatchmaking_RemoveFavoriteGame": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            typedefs.uint32,
            typedefs.uint16,
            typedefs.uint16,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamMatchmaking_RequestLobbyList": (typedefs.SteamAPICall_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListStringFilter": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListNumericalFilter": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListNearValueFilter": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable": (
        None,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListDistanceFilter": (
        None,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListResultCountFilter": (
        None,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_CreateLobby": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_JoinLobby": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_LeaveLobby": (None, (ctypes.c_void_p, typedefs.uint64_steamid)),
    "SteamAPI_ISteamMatchmaking_InviteUserToLobby": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_GetNumLobbyMembers": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyMemberByIndex": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyData": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyData": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyDataCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyDataByIndex": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamMatchmaking_DeleteLobbyData": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyMemberData": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyMemberData": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamMatchmaking_SendLobbyChatMsg": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyChatEntry": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_int,
            ctypes.POINTER(structs.CSteamID),
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamMatchmaking_RequestLobbyData": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyGameServer": (
        None,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            typedefs.uint32,
            typedefs.uint16,
            typedefs.uint64_steamid,
        ),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyGameServer": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint16),
            ctypes.POINTER(structs.CSteamID),
        ),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyMemberLimit": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyMemberLimit": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyType": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyJoinable": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_bool),
    ),
    "SteamAPI_ISteamMatchmaking_GetLobbyOwner": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_SetLobbyOwner": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmaking_SetLinkedLobby": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamMatchmakingServerListResponse_ServerResponded": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmakingServerListResponse_ServerFailedToRespond": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmakingServerListResponse_RefreshComplete": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmakingPingResponse_ServerResponded": (
        None,
        (ctypes.c_void_p, ctypes.POINTER(structs.gameserveritem_t)),
    ),
    "SteamAPI_ISteamMatchmakingPingResponse_ServerFailedToRespond": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmakingPlayersResponse_AddPlayerToList": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_float),
    ),
    "SteamAPI_ISteamMatchmakingPlayersResponse_PlayersFailedToRespond": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmakingPlayersResponse_PlayersRefreshComplete": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmakingRulesResponse_RulesResponded": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamMatchmakingRulesResponse_RulesFailedToRespond": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmakingRulesResponse_RulesRefreshComplete": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMatchmakingServerFriendsResponse_AddFriendToList": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.c_bool),
    ),
    "SteamAPI_ISteamMatchmakingServerFriendsResponse_FriendsFailedToRespond": (
        None,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamMatchmakingServerFriendsResponse_FriendsRefreshComplete": (
        None,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_SteamMatchmakingServers_v003": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamMatchmakingServers_RequestInternetServerList": (
        typedefs.HServerListRequest,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            ctypes.POINTER(ctypes.POINTER(structs.MatchMakingKeyValuePair_t)),
            typedefs.uint32,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamMatchmakingServers_RequestLANServerList": (
        typedefs.HServerListRequest,
        (ctypes.c_void_p, typedefs.AppId_t, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamMatchmakingServers_RequestFriendsServerList": (
        typedefs.HServerListRequest,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            ctypes.POINTER(ctypes.POINTER(structs.MatchMakingKeyValuePair_t)),
            typedefs.uint32,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamMatchmakingServers_RequestFavoritesServerList": (
        typedefs.HServerListRequest,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            ctypes.POINTER(ctypes.POINTER(structs.MatchMakingKeyValuePair_t)),
            typedefs.uint32,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamMatchmakingServers_RequestHistoryServerList": (
        typedefs.HServerListRequest,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            ctypes.POINTER(ctypes.POINTER(structs.MatchMakingKeyValuePair_t)),
            typedefs.uint32,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamMatchmakingServers_RequestSpectatorServerList": (
        typedefs.HServerListRequest,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            ctypes.POINTER(ctypes.POINTER(structs.MatchMakingKeyValuePair_t)),
            typedefs.uint32,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamMatchmakingServers_ReleaseRequest": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest),
    ),
    "SteamAPI_ISteamMatchmakingServers_GetServerDetails": (
        ctypes.POINTER(structs.gameserveritem_t),
        (ctypes.c_void_p, typedefs.HServerListRequest, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmakingServers_CancelQuery": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest),
    ),
    "SteamAPI_ISteamMatchmakingServers_RefreshQuery": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest),
    ),
    "SteamAPI_ISteamMatchmakingServers_IsRefreshing": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HServerListRequest),
    ),
    "SteamAPI_ISteamMatchmakingServers_GetServerCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.HServerListRequest),
    ),
    "SteamAPI_ISteamMatchmakingServers_RefreshServer": (
        None,
        (ctypes.c_void_p, typedefs.HServerListRequest, ctypes.c_int),
    ),
    "SteamAPI_ISteamMatchmakingServers_PingServer": (
        typedefs.HServerQuery,
        (ctypes.c_void_p, typedefs.uint32, typedefs.uint16, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamMatchmakingServers_PlayerDetails": (
        typedefs.HServerQuery,
        (ctypes.c_void_p, typedefs.uint32, typedefs.uint16, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamMatchmakingServers_ServerRules": (
        typedefs.HServerQuery,
        (ctypes.c_void_p, typedefs.uint32, typedefs.uint16, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamMatchmakingServers_ServerFriends": (
        typedefs.HServerQuery,
        (ctypes.c_void_p, typedefs.uint32, typedefs.uint16, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamMatchmakingServers_CancelServerQuery": (
        None,
        (ctypes.c_void_p, typedefs.HServerQuery),
    ),
    "SteamAPI_SteamParties_v002": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamParties_GetNumActiveBeacons": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamParties_GetBeaconByIndex": (
        typedefs.PartyBeaconID_t,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamParties_GetBeaconDetails": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.PartyBeaconID_t,
            ctypes.POINTER(structs.CSteamID),
            ctypes.POINTER(structs.SteamPartyBeaconLocation_t),
            ctypes.c_char_p,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamParties_JoinParty": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PartyBeaconID_t),
    ),
    "SteamAPI_ISteamParties_GetNumAvailableBeaconLocations": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.uint32)),
    ),
    "SteamAPI_ISteamParties_GetAvailableBeaconLocations": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamPartyBeaconLocation_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamParties_CreateBeacon": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(structs.SteamPartyBeaconLocation_t),
            ctypes.c_char_p,
            ctypes.c_char_p,
        ),
    ),
    "SteamAPI_ISteamParties_OnReservationCompleted": (
        None,
        (ctypes.c_void_p, typedefs.PartyBeaconID_t, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamParties_CancelReservation": (
        None,
        (ctypes.c_void_p, typedefs.PartyBeaconID_t, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamParties_ChangeNumOpenSlots": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PartyBeaconID_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamParties_DestroyBeacon": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PartyBeaconID_t),
    ),
    "SteamAPI_ISteamParties_GetBeaconLocationData": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            structs.SteamPartyBeaconLocation_t,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_SteamRemoteStorage_v016": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamRemoteStorage_FileWrite": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, typedefs.int32),
    ),
    "SteamAPI_ISteamRemoteStorage_FileRead": (
        typedefs.int32,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, typedefs.int32),
    ),
    "SteamAPI_ISteamRemoteStorage_FileWriteAsync": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_FileReadAsync": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p, typedefs.uint32, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_FileReadAsyncComplete": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SteamAPICall_t, ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_FileForget": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamRemoteStorage_FileDelete": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamRemoteStorage_FileShare": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_SetSyncPlatforms": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamRemoteStorage_FileWriteStreamOpen": (
        typedefs.UGCFileWriteStreamHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_FileWriteStreamWriteChunk": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCFileWriteStreamHandle_t, ctypes.c_void_p, typedefs.int32),
    ),
    "SteamAPI_ISteamRemoteStorage_FileWriteStreamClose": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCFileWriteStreamHandle_t),
    ),
    "SteamAPI_ISteamRemoteStorage_FileWriteStreamCancel": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCFileWriteStreamHandle_t),
    ),
    "SteamAPI_ISteamRemoteStorage_FileExists": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamRemoteStorage_FilePersisted": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_GetFileSize": (
        typedefs.int32,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_GetFileTimestamp": (
        typedefs.int64,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_GetSyncPlatforms": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_GetFileCount": (typedefs.int32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemoteStorage_GetFileNameAndSize": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(typedefs.int32)),
    ),
    "SteamAPI_ISteamRemoteStorage_GetQuota": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.uint64), ctypes.POINTER(typedefs.uint64)),
    ),
    "SteamAPI_ISteamRemoteStorage_IsCloudEnabledForAccount": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemoteStorage_IsCloudEnabledForApp": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemoteStorage_SetCloudEnabledForApp": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamRemoteStorage_UGCDownload": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.UGCHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_GetUGCDownloadProgress": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCHandle_t,
            ctypes.POINTER(typedefs.int32),
            ctypes.POINTER(typedefs.int32),
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_GetUGCDetails": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCHandle_t,
            ctypes.POINTER(typedefs.AppId_t),
            ctypes.POINTER(ctypes.c_char_p),
            ctypes.POINTER(typedefs.int32),
            ctypes.POINTER(structs.CSteamID),
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_UGCRead": (
        typedefs.int32,
        (
            ctypes.c_void_p,
            typedefs.UGCHandle_t,
            ctypes.c_void_p,
            typedefs.int32,
            typedefs.uint32,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_GetCachedUGCCount": (typedefs.int32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemoteStorage_GetCachedUGCHandle": (
        typedefs.UGCHandle_t,
        (ctypes.c_void_p, typedefs.int32),
    ),
    "SteamAPI_ISteamRemoteStorage_PublishWorkshopFile": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.AppId_t,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamParamStringArray_t),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_CreatePublishedFileUpdateRequest": (
        typedefs.PublishedFileUpdateHandle_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFileFile": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFilePreviewFile": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTitle": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFileDescription": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFileVisibility": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTags": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.PublishedFileUpdateHandle_t,
            ctypes.POINTER(structs.SteamParamStringArray_t),
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_CommitPublishedFileUpdate": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t),
    ),
    "SteamAPI_ISteamRemoteStorage_GetPublishedFileDetails": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_DeletePublishedFile": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamRemoteStorage_EnumerateUserPublishedFiles": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_SubscribePublishedFile": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamRemoteStorage_EnumerateUserSubscribedFiles": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_UnsubscribePublishedFile": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamRemoteStorage_GetPublishedItemVoteDetails": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamRemoteStorage_UpdateUserPublishedItemVote": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamRemoteStorage_GetUserPublishedItemVoteDetails": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            typedefs.uint32,
            ctypes.POINTER(structs.SteamParamStringArray_t),
            ctypes.POINTER(structs.SteamParamStringArray_t),
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_PublishVideo": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.AppId_t,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamParamStringArray_t),
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_SetUserPublishedFileAction": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamRemoteStorage_EnumeratePublishedFilesByUserAction": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_int, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_EnumeratePublishedWorkshopFiles": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            typedefs.uint32,
            typedefs.uint32,
            typedefs.uint32,
            ctypes.POINTER(structs.SteamParamStringArray_t),
            ctypes.POINTER(structs.SteamParamStringArray_t),
        ),
    ),
    "SteamAPI_ISteamRemoteStorage_UGCDownloadToLocation": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.UGCHandle_t, ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamRemoteStorage_GetLocalFileChangeCount": (typedefs.int32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemoteStorage_GetLocalFileChange": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)),
    ),
    "SteamAPI_ISteamRemoteStorage_BeginFileWriteBatch": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemoteStorage_EndFileWriteBatch": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_SteamUserStats_v013": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamUserStats_GetStatInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(typedefs.int32)),
    ),
    "SteamAPI_ISteamUserStats_GetStatFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_float)),
    ),
    "SteamAPI_ISteamUserStats_SetStatInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, typedefs.int32),
    ),
    "SteamAPI_ISteamUserStats_SetStatFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_float),
    ),
    "SteamAPI_ISteamUserStats_UpdateAvgRateStat": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_float, ctypes.c_double),
    ),
    "SteamAPI_ISteamUserStats_GetAchievement": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)),
    ),
    "SteamAPI_ISteamUserStats_SetAchievement": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamUserStats_ClearAchievement": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUserStats_GetAchievementAndUnlockTime": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.POINTER(ctypes.c_bool),
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamUserStats_StoreStats": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUserStats_GetAchievementIcon": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUserStats_GetAchievementDisplayAttribute": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUserStats_IndicateAchievementProgress": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, typedefs.uint32, typedefs.uint32),
    ),
    "SteamAPI_ISteamUserStats_GetNumAchievements": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUserStats_GetAchievementName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamUserStats_RequestUserStats": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamUserStats_GetUserStatInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.POINTER(typedefs.int32)),
    ),
    "SteamAPI_ISteamUserStats_GetUserStatFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.POINTER(ctypes.c_float)),
    ),
    "SteamAPI_ISteamUserStats_GetUserAchievement": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)),
    ),
    "SteamAPI_ISteamUserStats_GetUserAchievementAndUnlockTime": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_char_p,
            ctypes.POINTER(ctypes.c_bool),
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamUserStats_ResetAllStats": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamUserStats_FindOrCreateLeaderboard": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamUserStats_FindLeaderboard": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUserStats_GetLeaderboardName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.SteamLeaderboard_t),
    ),
    "SteamAPI_ISteamUserStats_GetLeaderboardEntryCount": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SteamLeaderboard_t),
    ),
    "SteamAPI_ISteamUserStats_GetLeaderboardSortMethod": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SteamLeaderboard_t),
    ),
    "SteamAPI_ISteamUserStats_GetLeaderboardDisplayType": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SteamLeaderboard_t),
    ),
    "SteamAPI_ISteamUserStats_DownloadLeaderboardEntries": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.SteamLeaderboard_t, ctypes.c_int, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamUserStats_DownloadLeaderboardEntriesForUsers": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            typedefs.SteamLeaderboard_t,
            ctypes.POINTER(structs.CSteamID),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamUserStats_GetDownloadedLeaderboardEntry": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamLeaderboardEntries_t,
            ctypes.c_int,
            ctypes.POINTER(structs.LeaderboardEntry_t),
            ctypes.POINTER(typedefs.int32),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamUserStats_UploadLeaderboardScore": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            typedefs.SteamLeaderboard_t,
            ctypes.c_int,
            typedefs.int32,
            ctypes.POINTER(typedefs.int32),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamUserStats_AttachLeaderboardUGC": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.SteamLeaderboard_t, typedefs.UGCHandle_t),
    ),
    "SteamAPI_ISteamUserStats_GetNumberOfCurrentPlayers": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamUserStats_RequestGlobalAchievementPercentages": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamUserStats_GetMostAchievedAchievementInfo": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.POINTER(ctypes.c_float),
            ctypes.POINTER(ctypes.c_bool),
        ),
    ),
    "SteamAPI_ISteamUserStats_GetNextMostAchievedAchievementInfo": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.POINTER(ctypes.c_float),
            ctypes.POINTER(ctypes.c_bool),
        ),
    ),
    "SteamAPI_ISteamUserStats_GetAchievementAchievedPercent": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_float)),
    ),
    "SteamAPI_ISteamUserStats_RequestGlobalStats": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamUserStats_GetGlobalStatInt64": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(typedefs.int64)),
    ),
    "SteamAPI_ISteamUserStats_GetGlobalStatDouble": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)),
    ),
    "SteamAPI_ISteamUserStats_GetGlobalStatHistoryInt64": (
        typedefs.int32,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(typedefs.int64), typedefs.uint32),
    ),
    "SteamAPI_ISteamUserStats_GetGlobalStatHistoryDouble": (
        typedefs.int32,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), typedefs.uint32),
    ),
    "SteamAPI_ISteamUserStats_GetAchievementProgressLimitsInt32": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.POINTER(typedefs.int32),
            ctypes.POINTER(typedefs.int32),
        ),
    ),
    "SteamAPI_ISteamUserStats_GetAchievementProgressLimitsFloat": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.POINTER(ctypes.c_float),
            ctypes.POINTER(ctypes.c_float),
        ),
    ),
    "SteamAPI_SteamApps_v009": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamApps_BIsSubscribed": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_BIsLowViolence": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_BIsCybercafe": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_BIsVACBanned": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_GetCurrentGameLanguage": (ctypes.c_char_p, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_GetAvailableGameLanguages": (ctypes.c_char_p, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_BIsSubscribedApp": (ctypes.c_bool, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_BIsDlcInstalled": (ctypes.c_bool, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_GetEarliestPurchaseUnixTime": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamApps_BIsSubscribedFromFreeWeekend": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_GetDLCCount": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_BGetDLCDataByIndex": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.AppId_t),
            ctypes.POINTER(ctypes.c_bool),
            ctypes.c_char_p,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamApps_InstallDLC": (None, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_UninstallDLC": (None, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_RequestAppProofOfPurchaseKey": (None, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_GetCurrentBetaName": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamApps_MarkContentCorrupt": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamApps_GetInstalledDepots": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.AppId_t, ctypes.POINTER(typedefs.DepotId_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamApps_GetAppInstallDir": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.AppId_t, ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamApps_BIsAppInstalled": (ctypes.c_bool, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_GetAppOwner": (typedefs.uint64_steamid, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_GetLaunchQueryParam": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamApps_GetDlcDownloadProgress": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.AppId_t,
            ctypes.POINTER(typedefs.uint64),
            ctypes.POINTER(typedefs.uint64),
        ),
    ),
    "SteamAPI_ISteamApps_GetAppBuildId": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_RequestAllProofOfPurchaseKeys": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_GetFileDetails": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamApps_GetLaunchCommandLine": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamApps_BIsSubscribedFromFamilySharing": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamApps_BIsTimedTrial": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.uint32), ctypes.POINTER(typedefs.uint32)),
    ),
    "SteamAPI_ISteamApps_SetDlcContext": (ctypes.c_bool, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamApps_GetNumBetas": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)),
    ),
    "SteamAPI_ISteamApps_GetBetaInfo": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint32),
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamApps_SetActiveBeta": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamApps_SetGamePerformanceSetting": (None, (ctypes.c_void_p, ctypes.c_int)),
    "SteamAPI_ISteamApps_SetGameRenderResolution": (
        None,
        (ctypes.c_void_p, typedefs.uint32, typedefs.uint32),
    ),
    "SteamAPI_SteamNetworking_v006": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerNetworking_v006": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamNetworking_SendP2PPacket": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_int,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworking_IsP2PPacketAvailable": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.uint32), ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworking_ReadP2PPacket": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(structs.CSteamID),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworking_AcceptP2PSessionWithUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamNetworking_CloseP2PSessionWithUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamNetworking_CloseP2PChannelWithUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworking_GetP2PSessionState": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.POINTER(structs.P2PSessionState_t)),
    ),
    "SteamAPI_ISteamNetworking_AllowP2PPacketRelay": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworking_CreateListenSocket": (
        typedefs.SNetListenSocket_t,
        (ctypes.c_void_p, ctypes.c_int, structs.SteamIPAddress_t, typedefs.uint16, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworking_CreateP2PConnectionSocket": (
        typedefs.SNetSocket_t,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_int, ctypes.c_int, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworking_CreateConnectionSocket": (
        typedefs.SNetSocket_t,
        (ctypes.c_void_p, structs.SteamIPAddress_t, typedefs.uint16, ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworking_DestroySocket": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SNetSocket_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworking_DestroyListenSocket": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SNetListenSocket_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworking_SendDataOnSocket": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SNetSocket_t, ctypes.c_void_p, typedefs.uint32, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworking_IsDataAvailableOnSocket": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SNetSocket_t, ctypes.POINTER(typedefs.uint32)),
    ),
    "SteamAPI_ISteamNetworking_RetrieveDataFromSocket": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SNetSocket_t,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamNetworking_IsDataAvailable": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SNetListenSocket_t,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.SNetSocket_t),
        ),
    ),
    "SteamAPI_ISteamNetworking_RetrieveData": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SNetListenSocket_t,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.SNetSocket_t),
        ),
    ),
    "SteamAPI_ISteamNetworking_GetSocketInfo": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SNetSocket_t,
            ctypes.POINTER(structs.CSteamID),
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(structs.SteamIPAddress_t),
            ctypes.POINTER(typedefs.uint16),
        ),
    ),
    "SteamAPI_ISteamNetworking_GetListenSocketInfo": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SNetListenSocket_t,
            ctypes.POINTER(structs.SteamIPAddress_t),
            ctypes.POINTER(typedefs.uint16),
        ),
    ),
    "SteamAPI_ISteamNetworking_GetSocketConnectionType": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SNetSocket_t),
    ),
    "SteamAPI_ISteamNetworking_GetMaxPacketSize": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SNetSocket_t),
    ),
    "SteamAPI_SteamScreenshots_v003": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamScreenshots_WriteScreenshot": (
        typedefs.ScreenshotHandle,
        (ctypes.c_void_p, ctypes.c_void_p, typedefs.uint32, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamScreenshots_AddScreenshotToLibrary": (
        typedefs.ScreenshotHandle,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamScreenshots_TriggerScreenshot": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamScreenshots_HookScreenshots": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamScreenshots_SetLocation": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.ScreenshotHandle, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamScreenshots_TagUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.ScreenshotHandle, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamScreenshots_TagPublishedFile": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.ScreenshotHandle, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamScreenshots_IsScreenshotsHooked": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamScreenshots_AddVRScreenshotToLibrary": (
        typedefs.ScreenshotHandle,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_SteamMusic_v001": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamMusic_BIsEnabled": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_BIsPlaying": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_GetPlaybackStatus": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_Play": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_Pause": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_PlayPrevious": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_PlayNext": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamMusic_SetVolume": (None, (ctypes.c_void_p, ctypes.c_float)),
    "SteamAPI_ISteamMusic_GetVolume": (ctypes.c_float, (ctypes.c_void_p,)),
    "SteamAPI_SteamHTTP_v003": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerHTTP_v003": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamHTTP_CreateHTTPRequest": (
        typedefs.HTTPRequestHandle,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestContextValue": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, typedefs.uint64),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestNetworkActivityTimeout": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, typedefs.uint32),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestHeaderValue": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestGetOrPostParameter": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTTP_SendHTTPRequest": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.POINTER(typedefs.SteamAPICall_t)),
    ),
    "SteamAPI_ISteamHTTP_SendHTTPRequestAndStreamResponse": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.POINTER(typedefs.SteamAPICall_t)),
    ),
    "SteamAPI_ISteamHTTP_DeferHTTPRequest": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle),
    ),
    "SteamAPI_ISteamHTTP_PrioritizeHTTPRequest": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPResponseHeaderSize": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HTTPRequestHandle,
            ctypes.c_char_p,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPResponseHeaderValue": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HTTPRequestHandle,
            ctypes.c_char_p,
            ctypes.POINTER(typedefs.uint8),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPResponseBodySize": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.POINTER(typedefs.uint32)),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPResponseBodyData": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HTTPRequestHandle,
            ctypes.POINTER(typedefs.uint8),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPStreamingResponseBodyData": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HTTPRequestHandle,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint8),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamHTTP_ReleaseHTTPRequest": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPDownloadProgressPct": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.POINTER(ctypes.c_float)),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestRawPostBody": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HTTPRequestHandle,
            ctypes.c_char_p,
            ctypes.POINTER(typedefs.uint8),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamHTTP_CreateCookieContainer": (
        typedefs.HTTPCookieContainerHandle,
        (ctypes.c_void_p, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTTP_ReleaseCookieContainer": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPCookieContainerHandle),
    ),
    "SteamAPI_ISteamHTTP_SetCookie": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HTTPCookieContainerHandle,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
        ),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestCookieContainer": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, typedefs.HTTPCookieContainerHandle),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestUserAgentInfo": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, typedefs.uint32),
    ),
    "SteamAPI_ISteamHTTP_GetHTTPRequestWasTimedOut": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HTTPRequestHandle, ctypes.POINTER(ctypes.c_bool)),
    ),
    "SteamAPI_SteamInput_v007": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamInput_Init": (ctypes.c_bool, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamInput_Shutdown": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInput_SetInputActionManifestFilePath": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamInput_RunFrame": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamInput_BWaitForData": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_bool, typedefs.uint32),
    ),
    "SteamAPI_ISteamInput_BNewDataAvailable": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInput_GetConnectedControllers": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.InputHandle_t)),
    ),
    "SteamAPI_ISteamInput_EnableDeviceCallbacks": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInput_EnableActionEventCallbacks": (
        None,
        (ctypes.c_void_p, typedefs.SteamInputActionEventCallbackPointer),
    ),
    "SteamAPI_ISteamInput_GetActionSetHandle": (
        typedefs.InputActionSetHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamInput_ActivateActionSet": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, typedefs.InputActionSetHandle_t),
    ),
    "SteamAPI_ISteamInput_GetCurrentActionSet": (
        typedefs.InputActionSetHandle_t,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_ActivateActionSetLayer": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, typedefs.InputActionSetHandle_t),
    ),
    "SteamAPI_ISteamInput_DeactivateActionSetLayer": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, typedefs.InputActionSetHandle_t),
    ),
    "SteamAPI_ISteamInput_DeactivateAllActionSetLayers": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_GetActiveActionSetLayers": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.InputHandle_t, ctypes.POINTER(typedefs.InputActionSetHandle_t)),
    ),
    "SteamAPI_ISteamInput_GetDigitalActionHandle": (
        typedefs.InputDigitalActionHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamInput_GetDigitalActionData": (
        structs.InputDigitalActionData_t,
        (ctypes.c_void_p, typedefs.InputHandle_t, typedefs.InputDigitalActionHandle_t),
    ),
    "SteamAPI_ISteamInput_GetDigitalActionOrigins": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            typedefs.InputActionSetHandle_t,
            typedefs.InputDigitalActionHandle_t,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamInput_GetStringForDigitalActionName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.InputDigitalActionHandle_t),
    ),
    "SteamAPI_ISteamInput_GetAnalogActionHandle": (
        typedefs.InputAnalogActionHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamInput_GetAnalogActionData": (
        structs.InputAnalogActionData_t,
        (ctypes.c_void_p, typedefs.InputHandle_t, typedefs.InputAnalogActionHandle_t),
    ),
    "SteamAPI_ISteamInput_GetAnalogActionOrigins": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            typedefs.InputActionSetHandle_t,
            typedefs.InputAnalogActionHandle_t,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamInput_GetGlyphPNGForActionOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, typedefs.uint32),
    ),
    "SteamAPI_ISteamInput_GetGlyphSVGForActionOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int, typedefs.uint32),
    ),
    "SteamAPI_ISteamInput_GetGlyphForActionOrigin_Legacy": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_GetStringForActionOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_GetStringForAnalogActionName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.InputAnalogActionHandle_t),
    ),
    "SteamAPI_ISteamInput_StopAnalogActionMomentum": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, typedefs.InputAnalogActionHandle_t),
    ),
    "SteamAPI_ISteamInput_GetMotionData": (
        structs.InputMotionData_t,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_TriggerVibration": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, ctypes.c_ushort, ctypes.c_ushort),
    ),
    "SteamAPI_ISteamInput_TriggerVibrationExtended": (
        None,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            ctypes.c_ushort,
            ctypes.c_ushort,
            ctypes.c_ushort,
            ctypes.c_ushort,
        ),
    ),
    "SteamAPI_ISteamInput_TriggerSimpleHapticEvent": (
        None,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            ctypes.c_int,
            typedefs.uint8,
            ctypes.c_char,
            typedefs.uint8,
            ctypes.c_char,
        ),
    ),
    "SteamAPI_ISteamInput_SetLEDColor": (
        None,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            typedefs.uint8,
            typedefs.uint8,
            typedefs.uint8,
            ctypes.c_uint,
        ),
    ),
    "SteamAPI_ISteamInput_Legacy_TriggerHapticPulse": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, ctypes.c_int, ctypes.c_ushort),
    ),
    "SteamAPI_ISteamInput_Legacy_TriggerRepeatedHapticPulse": (
        None,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            ctypes.c_int,
            ctypes.c_ushort,
            ctypes.c_ushort,
            ctypes.c_ushort,
            ctypes.c_uint,
        ),
    ),
    "SteamAPI_ISteamInput_ShowBindingPanel": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_GetInputTypeForHandle": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_GetControllerForGamepadIndex": (
        typedefs.InputHandle_t,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_GetGamepadIndexForController": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_GetStringForXboxOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_GetGlyphForXboxOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_GetActionOriginFromXboxOrigin": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.InputHandle_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_TranslateActionOrigin": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamInput_GetDeviceBindingRevision": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.InputHandle_t,
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamInput_GetRemotePlaySessionID": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.InputHandle_t),
    ),
    "SteamAPI_ISteamInput_GetSessionInputConfigurationSettings": (
        typedefs.uint16,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamInput_SetDualSenseTriggerEffect": (
        None,
        (ctypes.c_void_p, typedefs.InputHandle_t, ctypes.c_void_p),
    ),
    "SteamAPI_SteamController_v008": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamController_Init": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamController_Shutdown": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamController_RunFrame": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamController_GetConnectedControllers": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.ControllerHandle_t)),
    ),
    "SteamAPI_ISteamController_GetActionSetHandle": (
        typedefs.ControllerActionSetHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamController_ActivateActionSet": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, typedefs.ControllerActionSetHandle_t),
    ),
    "SteamAPI_ISteamController_GetCurrentActionSet": (
        typedefs.ControllerActionSetHandle_t,
        (ctypes.c_void_p, typedefs.ControllerHandle_t),
    ),
    "SteamAPI_ISteamController_ActivateActionSetLayer": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, typedefs.ControllerActionSetHandle_t),
    ),
    "SteamAPI_ISteamController_DeactivateActionSetLayer": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, typedefs.ControllerActionSetHandle_t),
    ),
    "SteamAPI_ISteamController_DeactivateAllActionSetLayers": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t),
    ),
    "SteamAPI_ISteamController_GetActiveActionSetLayers": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.ControllerHandle_t,
            ctypes.POINTER(typedefs.ControllerActionSetHandle_t),
        ),
    ),
    "SteamAPI_ISteamController_GetDigitalActionHandle": (
        typedefs.ControllerDigitalActionHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamController_GetDigitalActionData": (
        structs.InputDigitalActionData_t,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, typedefs.ControllerDigitalActionHandle_t),
    ),
    "SteamAPI_ISteamController_GetDigitalActionOrigins": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.ControllerHandle_t,
            typedefs.ControllerActionSetHandle_t,
            typedefs.ControllerDigitalActionHandle_t,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamController_GetAnalogActionHandle": (
        typedefs.ControllerAnalogActionHandle_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamController_GetAnalogActionData": (
        structs.InputAnalogActionData_t,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, typedefs.ControllerAnalogActionHandle_t),
    ),
    "SteamAPI_ISteamController_GetAnalogActionOrigins": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.ControllerHandle_t,
            typedefs.ControllerActionSetHandle_t,
            typedefs.ControllerAnalogActionHandle_t,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamController_GetGlyphForActionOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_GetStringForActionOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_StopAnalogActionMomentum": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, typedefs.ControllerAnalogActionHandle_t),
    ),
    "SteamAPI_ISteamController_GetMotionData": (
        structs.InputMotionData_t,
        (ctypes.c_void_p, typedefs.ControllerHandle_t),
    ),
    "SteamAPI_ISteamController_TriggerHapticPulse": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, ctypes.c_int, ctypes.c_ushort),
    ),
    "SteamAPI_ISteamController_TriggerRepeatedHapticPulse": (
        None,
        (
            ctypes.c_void_p,
            typedefs.ControllerHandle_t,
            ctypes.c_int,
            ctypes.c_ushort,
            ctypes.c_ushort,
            ctypes.c_ushort,
            ctypes.c_uint,
        ),
    ),
    "SteamAPI_ISteamController_TriggerVibration": (
        None,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, ctypes.c_ushort, ctypes.c_ushort),
    ),
    "SteamAPI_ISteamController_SetLEDColor": (
        None,
        (
            ctypes.c_void_p,
            typedefs.ControllerHandle_t,
            typedefs.uint8,
            typedefs.uint8,
            typedefs.uint8,
            ctypes.c_uint,
        ),
    ),
    "SteamAPI_ISteamController_ShowBindingPanel": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.ControllerHandle_t),
    ),
    "SteamAPI_ISteamController_GetInputTypeForHandle": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.ControllerHandle_t),
    ),
    "SteamAPI_ISteamController_GetControllerForGamepadIndex": (
        typedefs.ControllerHandle_t,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_GetGamepadIndexForController": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.ControllerHandle_t),
    ),
    "SteamAPI_ISteamController_GetStringForXboxOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_GetGlyphForXboxOrigin": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_GetActionOriginFromXboxOrigin": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.ControllerHandle_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_TranslateActionOrigin": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamController_GetControllerBindingRevision": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.ControllerHandle_t,
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_SteamUGC_v021": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerUGC_v021": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamUGC_CreateQueryUserUGCRequest": (
        typedefs.UGCQueryHandle_t,
        (
            ctypes.c_void_p,
            typedefs.AccountID_t,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            typedefs.AppId_t,
            typedefs.AppId_t,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_CreateQueryAllUGCRequestPage": (
        typedefs.UGCQueryHandle_t,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            typedefs.AppId_t,
            typedefs.AppId_t,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_CreateQueryAllUGCRequestCursor": (
        typedefs.UGCQueryHandle_t,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            typedefs.AppId_t,
            typedefs.AppId_t,
            ctypes.c_char_p,
        ),
    ),
    "SteamAPI_ISteamUGC_CreateQueryUGCDetailsRequest": (
        typedefs.UGCQueryHandle_t,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.PublishedFileId_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_SendQueryUGCRequest": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCResult": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.POINTER(structs.SteamUGCDetails_t),
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCNumTags": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCTag": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCTagDisplayName": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCPreviewURL": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCMetadata": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCChildren": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.POINTER(typedefs.PublishedFileId_t),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCStatistic": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint64),
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCNumAdditionalPreviews": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCAdditionalPreview": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCNumKeyValueTags": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCKeyValueTag": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryFirstUGCKeyValueTag": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetNumSupportedGameVersions": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_GetSupportedGameVersionData": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            typedefs.uint32,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_GetQueryUGCContentDescriptors": (
        typedefs.uint32,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            typedefs.uint32,
            ctypes.POINTER(ctypes.c_int),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamUGC_ReleaseQueryUGCRequest": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t),
    ),
    "SteamAPI_ISteamUGC_AddRequiredTag": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_AddRequiredTagGroup": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCQueryHandle_t,
            ctypes.POINTER(structs.SteamParamStringArray_t),
        ),
    ),
    "SteamAPI_ISteamUGC_AddExcludedTag": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetReturnOnlyIDs": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnKeyValueTags": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnLongDescription": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnMetadata": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnChildren": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnAdditionalPreviews": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnTotalOnly": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetReturnPlaytimeStats": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_SetLanguage": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetAllowCachedResponse": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_SetAdminQuery": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetCloudFileNameFilter": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetMatchAnyTag": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_SetSearchText": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetRankedByTrendDays": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_SetTimeCreatedDateRange": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.RTime32, typedefs.RTime32),
    ),
    "SteamAPI_ISteamUGC_SetTimeUpdatedDateRange": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, typedefs.RTime32, typedefs.RTime32),
    ),
    "SteamAPI_ISteamUGC_AddRequiredKeyValueTag": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCQueryHandle_t, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_RequestUGCDetails": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_CreateItem": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.AppId_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamUGC_StartItemUpdate": (
        typedefs.UGCUpdateHandle_t,
        (ctypes.c_void_p, typedefs.AppId_t, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_SetItemTitle": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetItemDescription": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetItemUpdateLanguage": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetItemMetadata": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetItemVisibility": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamUGC_SetItemTags": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.UGCUpdateHandle_t,
            ctypes.POINTER(structs.SteamParamStringArray_t),
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamUGC_SetItemContent": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetItemPreview": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SetAllowLegacyUpload": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_RemoveAllItemKeyValueTags": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t),
    ),
    "SteamAPI_ISteamUGC_RemoveItemKeyValueTags": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_AddItemKeyValueTag": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_AddItemPreviewFile": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamUGC_AddItemPreviewVideo": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_UpdateItemPreviewFile": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, typedefs.uint32, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_UpdateItemPreviewVideo": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, typedefs.uint32, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_RemoveItemPreview": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_AddContentDescriptor": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamUGC_RemoveContentDescriptor": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_int),
    ),
    "SteamAPI_ISteamUGC_SetRequiredGameVersions": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SubmitItemUpdate": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.UGCUpdateHandle_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_GetItemUpdateProgress": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.UGCUpdateHandle_t,
            ctypes.POINTER(typedefs.uint64),
            ctypes.POINTER(typedefs.uint64),
        ),
    ),
    "SteamAPI_ISteamUGC_SetUserItemVote": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_GetUserItemVote": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_AddItemToFavorites": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.AppId_t, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_RemoveItemFromFavorites": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.AppId_t, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_SubscribeItem": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_UnsubscribeItem": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_GetNumSubscribedItems": (typedefs.uint32, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamUGC_GetSubscribedItems": (
        typedefs.uint32,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.PublishedFileId_t),
            typedefs.uint32,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamUGC_GetItemState": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_GetItemInstallInfo": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.PublishedFileId_t,
            ctypes.POINTER(typedefs.uint64),
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamUGC_GetItemDownloadInfo": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.PublishedFileId_t,
            ctypes.POINTER(typedefs.uint64),
            ctypes.POINTER(typedefs.uint64),
        ),
    ),
    "SteamAPI_ISteamUGC_DownloadItem": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamUGC_BInitWorkshopForGameServer": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.DepotId_t, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamUGC_SuspendDownloads": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamUGC_StartPlaytimeTracking": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.PublishedFileId_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_StopPlaytimeTracking": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.PublishedFileId_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_StopPlaytimeTrackingForAllItems": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamUGC_AddDependency": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_RemoveDependency": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_AddAppDependency": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamUGC_RemoveAppDependency": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamUGC_GetAppDependencies": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_DeleteItem": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_ShowWorkshopEULA": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUGC_GetWorkshopEULAStatus": (typedefs.SteamAPICall_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUGC_GetUserContentDescriptorPreferences": (
        typedefs.uint32,
        (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_SetItemsDisabledLocally": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.PublishedFileId_t),
            typedefs.uint32,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamUGC_SetSubscriptionsLoadOrder": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.PublishedFileId_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamUGC_MarkDownloadedItemAsUnused": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.PublishedFileId_t),
    ),
    "SteamAPI_ISteamUGC_GetNumDownloadedItems": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamUGC_GetDownloadedItems": (
        typedefs.uint32,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.PublishedFileId_t), typedefs.uint32),
    ),
    "SteamAPI_SteamHTMLSurface_v005": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamHTMLSurface_Init": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamHTMLSurface_Shutdown": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamHTMLSurface_CreateBrowser": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTMLSurface_RemoveBrowser": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_LoadURL": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTMLSurface_SetSize": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.uint32, typedefs.uint32),
    ),
    "SteamAPI_ISteamHTMLSurface_StopLoad": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_Reload": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_GoBack": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_GoForward": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_AddHeader": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTMLSurface_ExecuteJavascript": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamHTMLSurface_MouseUp": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_MouseDown": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_MouseDoubleClick": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_MouseMove": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_MouseWheel": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.int32),
    ),
    "SteamAPI_ISteamHTMLSurface_KeyDown": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.uint32, ctypes.c_int, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTMLSurface_KeyUp": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.uint32, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_KeyChar": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.uint32, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_SetHorizontalScroll": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.uint32),
    ),
    "SteamAPI_ISteamHTMLSurface_SetVerticalScroll": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, typedefs.uint32),
    ),
    "SteamAPI_ISteamHTMLSurface_SetKeyFocus": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTMLSurface_ViewSource": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_CopyToClipboard": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_PasteFromClipboard": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser),
    ),
    "SteamAPI_ISteamHTMLSurface_Find": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTMLSurface_StopFind": (None, (ctypes.c_void_p, typedefs.HHTMLBrowser)),
    "SteamAPI_ISteamHTMLSurface_GetLinkAtPosition": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_SetCookie": (
        None,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.RTime32,
            ctypes.c_bool,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamHTMLSurface_SetPageScaleFactor": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_float, ctypes.c_int, ctypes.c_int),
    ),
    "SteamAPI_ISteamHTMLSurface_SetBackgroundMode": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTMLSurface_SetDPIScalingFactor": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_float),
    ),
    "SteamAPI_ISteamHTMLSurface_OpenDeveloperTools": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser),
    ),
    "SteamAPI_ISteamHTMLSurface_AllowStartRequest": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTMLSurface_JSDialogResponse": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.c_bool),
    ),
    "SteamAPI_ISteamHTMLSurface_FileLoadDialogResponse": (
        None,
        (ctypes.c_void_p, typedefs.HHTMLBrowser, ctypes.POINTER(ctypes.c_char_p)),
    ),
    "SteamAPI_SteamInventory_v003": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerInventory_v003": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamInventory_GetResultStatus": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SteamInventoryResult_t),
    ),
    "SteamAPI_ISteamInventory_GetResultItems": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryResult_t,
            ctypes.POINTER(structs.SteamItemDetails_t),
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamInventory_GetResultItemProperty": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryResult_t,
            typedefs.uint32,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamInventory_GetResultTimestamp": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.SteamInventoryResult_t),
    ),
    "SteamAPI_ISteamInventory_CheckResultSteamID": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.SteamInventoryResult_t, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamInventory_DestroyResult": (
        None,
        (ctypes.c_void_p, typedefs.SteamInventoryResult_t),
    ),
    "SteamAPI_ISteamInventory_GetAllItems": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamInventoryResult_t)),
    ),
    "SteamAPI_ISteamInventory_GetItemsByID": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            ctypes.POINTER(typedefs.SteamItemInstanceID_t),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_SerializeResult": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryResult_t,
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamInventory_DeserializeResult": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamInventory_GenerateItems": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            ctypes.POINTER(typedefs.SteamItemDef_t),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_GrantPromoItems": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamInventoryResult_t)),
    ),
    "SteamAPI_ISteamInventory_AddPromoItem": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamInventoryResult_t), typedefs.SteamItemDef_t),
    ),
    "SteamAPI_ISteamInventory_AddPromoItems": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            ctypes.POINTER(typedefs.SteamItemDef_t),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_ConsumeItem": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            typedefs.SteamItemInstanceID_t,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_ExchangeItems": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            ctypes.POINTER(typedefs.SteamItemDef_t),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
            ctypes.POINTER(typedefs.SteamItemInstanceID_t),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_TransferItemQuantity": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            typedefs.SteamItemInstanceID_t,
            typedefs.uint32,
            typedefs.SteamItemInstanceID_t,
        ),
    ),
    "SteamAPI_ISteamInventory_SendItemDropHeartbeat": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInventory_TriggerItemDrop": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamInventoryResult_t), typedefs.SteamItemDef_t),
    ),
    "SteamAPI_ISteamInventory_TradeItems": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
            typedefs.uint64_steamid,
            ctypes.POINTER(typedefs.SteamItemInstanceID_t),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
            ctypes.POINTER(typedefs.SteamItemInstanceID_t),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_LoadItemDefinitions": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInventory_GetItemDefinitionIDs": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamItemDef_t), ctypes.POINTER(typedefs.uint32)),
    ),
    "SteamAPI_ISteamInventory_GetItemDefinitionProperty": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamItemDef_t,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamInventory_RequestEligiblePromoItemDefinitionsIDs": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamInventory_GetEligiblePromoItemDefinitionIDs": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.POINTER(typedefs.SteamItemDef_t),
            ctypes.POINTER(typedefs.uint32),
        ),
    ),
    "SteamAPI_ISteamInventory_StartPurchase": (
        typedefs.SteamAPICall_t,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamItemDef_t),
            ctypes.POINTER(typedefs.uint32),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_RequestPrices": (typedefs.SteamAPICall_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInventory_GetNumItemsWithPrices": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamInventory_GetItemsWithPrices": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamItemDef_t),
            ctypes.POINTER(typedefs.uint64),
            ctypes.POINTER(typedefs.uint64),
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamInventory_GetItemPrice": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamItemDef_t,
            ctypes.POINTER(typedefs.uint64),
            ctypes.POINTER(typedefs.uint64),
        ),
    ),
    "SteamAPI_ISteamInventory_StartUpdateProperties": (
        typedefs.SteamInventoryUpdateHandle_t,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamInventory_RemoveProperty": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryUpdateHandle_t,
            typedefs.SteamItemInstanceID_t,
            ctypes.c_char_p,
        ),
    ),
    "SteamAPI_ISteamInventory_SetPropertyString": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryUpdateHandle_t,
            typedefs.SteamItemInstanceID_t,
            ctypes.c_char_p,
            ctypes.c_char_p,
        ),
    ),
    "SteamAPI_ISteamInventory_SetPropertyBool": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryUpdateHandle_t,
            typedefs.SteamItemInstanceID_t,
            ctypes.c_char_p,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamInventory_SetPropertyInt64": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryUpdateHandle_t,
            typedefs.SteamItemInstanceID_t,
            ctypes.c_char_p,
            typedefs.int64,
        ),
    ),
    "SteamAPI_ISteamInventory_SetPropertyFloat": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryUpdateHandle_t,
            typedefs.SteamItemInstanceID_t,
            ctypes.c_char_p,
            ctypes.c_float,
        ),
    ),
    "SteamAPI_ISteamInventory_SubmitUpdateProperties": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.SteamInventoryUpdateHandle_t,
            ctypes.POINTER(typedefs.SteamInventoryResult_t),
        ),
    ),
    "SteamAPI_ISteamInventory_InspectItem": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamInventoryResult_t), ctypes.c_char_p),
    ),
    "SteamAPI_SteamTimeline_v004": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamTimeline_SetTimelineTooltip": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_float),
    ),
    "SteamAPI_ISteamTimeline_ClearTimelineTooltip": (None, (ctypes.c_void_p, ctypes.c_float)),
    "SteamAPI_ISteamTimeline_SetTimelineGameMode": (None, (ctypes.c_void_p, ctypes.c_int)),
    "SteamAPI_ISteamTimeline_AddInstantaneousTimelineEvent": (
        typedefs.TimelineEventHandle_t,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_float,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamTimeline_AddRangeTimelineEvent": (
        typedefs.TimelineEventHandle_t,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_float,
            ctypes.c_float,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamTimeline_StartRangeTimelineEvent": (
        typedefs.TimelineEventHandle_t,
        (
            ctypes.c_void_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_float,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamTimeline_UpdateRangeTimelineEvent": (
        None,
        (
            ctypes.c_void_p,
            typedefs.TimelineEventHandle_t,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamTimeline_EndRangeTimelineEvent": (
        None,
        (ctypes.c_void_p, typedefs.TimelineEventHandle_t, ctypes.c_float),
    ),
    "SteamAPI_ISteamTimeline_RemoveTimelineEvent": (
        None,
        (ctypes.c_void_p, typedefs.TimelineEventHandle_t),
    ),
    "SteamAPI_ISteamTimeline_DoesEventRecordingExist": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.TimelineEventHandle_t),
    ),
    "SteamAPI_ISteamTimeline_StartGamePhase": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamTimeline_EndGamePhase": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamTimeline_SetGamePhaseID": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamTimeline_DoesGamePhaseRecordingExist": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamTimeline_AddGamePhaseTag": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamTimeline_SetGamePhaseAttribute": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamTimeline_OpenOverlayToGamePhase": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamTimeline_OpenOverlayToTimelineEvent": (
        None,
        (ctypes.c_void_p, typedefs.TimelineEventHandle_t),
    ),
    "SteamAPI_SteamVideo_v007": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamVideo_GetVideoURL": (None, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamVideo_IsBroadcasting": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)),
    ),
    "SteamAPI_ISteamVideo_GetOPFSettings": (None, (ctypes.c_void_p, typedefs.AppId_t)),
    "SteamAPI_ISteamVideo_GetOPFStringForApp": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.AppId_t, ctypes.c_char_p, ctypes.POINTER(typedefs.int32)),
    ),
    "SteamAPI_SteamParentalSettings_v001": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamParentalSettings_BIsParentalLockEnabled": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamParentalSettings_BIsParentalLockLocked": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamParentalSettings_BIsAppBlocked": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamParentalSettings_BIsAppInBlockList": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamParentalSettings_BIsFeatureBlocked": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamParentalSettings_BIsFeatureInBlockList": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_SteamRemotePlay_v004": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamRemotePlay_GetSessionCount": (typedefs.uint32, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemotePlay_GetSessionID": (
        typedefs.RemotePlaySessionID_t,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamRemotePlay_BSessionRemotePlayTogether": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetSessionSteamID": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetSessionGuestID": (
        typedefs.uint32,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetSmallSessionAvatar": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetMediumSessionAvatar": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetLargeSessionAvatar": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetSessionClientName": (
        ctypes.c_char_p,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_GetSessionClientFormFactor": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t),
    ),
    "SteamAPI_ISteamRemotePlay_BGetSessionClientResolution": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.RemotePlaySessionID_t,
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(ctypes.c_int),
        ),
    ),
    "SteamAPI_ISteamRemotePlay_ShowRemotePlayTogetherUI": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemotePlay_BSendRemotePlayTogetherInvite": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamRemotePlay_BEnableRemotePlayTogetherDirectInput": (
        ctypes.c_bool,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamRemotePlay_DisableRemotePlayTogetherDirectInput": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamRemotePlay_GetInput": (
        typedefs.uint32,
        (ctypes.c_void_p, ctypes.POINTER(structs.RemotePlayInput_t), typedefs.uint32),
    ),
    "SteamAPI_ISteamRemotePlay_SetMouseVisibility": (
        None,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t, ctypes.c_bool),
    ),
    "SteamAPI_ISteamRemotePlay_SetMousePosition": (
        None,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t, ctypes.c_float, ctypes.c_float),
    ),
    "SteamAPI_ISteamRemotePlay_CreateMouseCursor": (
        typedefs.RemotePlayCursorID_t,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_void_p,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamRemotePlay_SetMouseCursor": (
        None,
        (ctypes.c_void_p, typedefs.RemotePlaySessionID_t, typedefs.RemotePlayCursorID_t),
    ),
    "SteamAPI_SteamNetworkingMessages_SteamAPI_v002": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerNetworkingMessages_SteamAPI_v002": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamNetworkingMessages_SendMessageToUser": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_int,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingMessages_ReceiveMessagesOnChannel": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(ctypes.POINTER(structs.SteamNetworkingMessage_t)),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingMessages_AcceptSessionWithUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIdentity)),
    ),
    "SteamAPI_ISteamNetworkingMessages_CloseSessionWithUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIdentity)),
    ),
    "SteamAPI_ISteamNetworkingMessages_CloseChannelWithUser": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworkingMessages_GetSessionConnectionInfo": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.POINTER(structs.SteamNetConnectionInfo_t),
            ctypes.POINTER(structs.SteamNetConnectionRealTimeStatus_t),
        ),
    ),
    "SteamAPI_SteamNetworkingSockets_SteamAPI_v013": (ctypes.c_void_p, ()),
    "SteamAPI_SteamGameServerNetworkingSockets_SteamAPI_v013": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamNetworkingSockets_CreateListenSocketIP": (
        typedefs.HSteamListenSocket,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ConnectByIPAddress": (
        typedefs.HSteamNetConnection,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2P": (
        typedefs.HSteamListenSocket,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ConnectP2P": (
        typedefs.HSteamNetConnection,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_AcceptConnection": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.HSteamNetConnection),
    ),
    "SteamAPI_ISteamNetworkingSockets_CloseConnection": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_CloseListenSocket": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamListenSocket),
    ),
    "SteamAPI_ISteamNetworkingSockets_SetConnectionUserData": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, typedefs.int64),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetConnectionUserData": (
        typedefs.int64,
        (ctypes.c_void_p, typedefs.HSteamNetConnection),
    ),
    "SteamAPI_ISteamNetworkingSockets_SetConnectionName": (
        None,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetConnectionName": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworkingSockets_SendMessageToConnection": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_int,
            ctypes.POINTER(typedefs.int64),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_SendMessages": (
        None,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(ctypes.POINTER(structs.SteamNetworkingMessage_t)),
            ctypes.POINTER(typedefs.int64),
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_FlushMessagesOnConnection": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.HSteamNetConnection),
    ),
    "SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnConnection": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.POINTER(ctypes.POINTER(structs.SteamNetworkingMessage_t)),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetConnectionInfo": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.POINTER(structs.SteamNetConnectionInfo_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetConnectionRealTimeStatus": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.POINTER(structs.SteamNetConnectionRealTimeStatus_t),
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetConnectionRealTimeLaneStatus_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetDetailedConnectionStatus": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, ctypes.c_char_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetListenSocketAddress": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.HSteamListenSocket,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_CreateSocketPair": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.HSteamNetConnection),
            ctypes.POINTER(typedefs.HSteamNetConnection),
            ctypes.c_bool,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.POINTER(structs.SteamNetworkingIdentity),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ConfigureConnectionLanes": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int),
            ctypes.POINTER(typedefs.uint16),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetIdentity": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIdentity)),
    ),
    "SteamAPI_ISteamNetworkingSockets_InitAuthentication": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamNetworkingSockets_GetAuthenticationStatus": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetAuthenticationStatus_t)),
    ),
    "SteamAPI_ISteamNetworkingSockets_CreatePollGroup": (
        typedefs.HSteamNetPollGroup,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamNetworkingSockets_DestroyPollGroup": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetPollGroup),
    ),
    "SteamAPI_ISteamNetworkingSockets_SetConnectionPollGroup": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, typedefs.HSteamNetPollGroup),
    ),
    "SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnPollGroup": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetPollGroup,
            ctypes.POINTER(ctypes.POINTER(structs.SteamNetworkingMessage_t)),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ReceivedRelayAuthTicket": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamNetworkingSockets_FindRelayAuthTicketForServer": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.c_int,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ConnectToHostedDedicatedServer": (
        typedefs.HSteamNetConnection,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPort": (
        typedefs.uint16,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPOPID": (
        typedefs.SteamNetworkingPOPID,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerAddress": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamDatagramHostedAddress)),
    ),
    "SteamAPI_ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket": (
        typedefs.HSteamListenSocket,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetGameCoordinatorServerLogin": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamDatagramGameCoordinatorServerLogin),
            ctypes.POINTER(ctypes.c_int),
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ConnectP2PCustomSignaling": (
        typedefs.HSteamNetConnection,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ReceivedP2PCustomSignal": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetCertificateRequest": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_int),
            ctypes.c_void_p,
            ctypes.POINTER(typedefs.SteamNetworkingErrMsg),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_SetCertificate": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.SteamNetworkingErrMsg),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_ResetIdentity": (
        None,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIdentity)),
    ),
    "SteamAPI_ISteamNetworkingSockets_RunCallbacks": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamNetworkingSockets_BeginAsyncRequestFakeIP": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetFakeIP": (
        None,
        (ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(structs.SteamNetworkingFakeIPResult_t)),
    ),
    "SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2PFakeIP": (
        typedefs.HSteamListenSocket,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_GetRemoteFakeIPForConnection": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.HSteamNetConnection,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
        ),
    ),
    "SteamAPI_ISteamNetworkingSockets_CreateFakeUDPPort": (
        ctypes.c_void_p,
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_SteamNetworkingUtils_SteamAPI_v004": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamNetworkingUtils_AllocateMessage": (
        ctypes.POINTER(structs.SteamNetworkingMessage_t),
        (ctypes.c_void_p, ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworkingUtils_InitRelayNetworkAccess": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamNetworkingUtils_GetRelayNetworkStatus": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamRelayNetworkStatus_t)),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetLocalPingLocation": (
        ctypes.c_float,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkPingLocation_t)),
    ),
    "SteamAPI_ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkPingLocation_t),
            ctypes.POINTER(structs.SteamNetworkPingLocation_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_EstimatePingTimeFromLocalHost": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkPingLocation_t)),
    ),
    "SteamAPI_ISteamNetworkingUtils_ConvertPingLocationToString": (
        None,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkPingLocation_t),
            ctypes.c_char_p,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_ParsePingLocationString": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(structs.SteamNetworkPingLocation_t)),
    ),
    "SteamAPI_ISteamNetworkingUtils_CheckPingDataUpToDate": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_float),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetPingToDataCenter": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            typedefs.SteamNetworkingPOPID,
            ctypes.POINTER(typedefs.SteamNetworkingPOPID),
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetDirectPingToPOP": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.SteamNetworkingPOPID),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetPOPCount": (ctypes.c_int, (ctypes.c_void_p,)),
    "SteamAPI_ISteamNetworkingUtils_GetPOPList": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(typedefs.SteamNetworkingPOPID), ctypes.c_int),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetLocalTimestamp": (
        typedefs.SteamNetworkingMicroseconds,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetDebugOutputFunction": (
        None,
        (ctypes.c_void_p, ctypes.c_int, typedefs.FSteamNetworkingSocketsDebugOutput),
    ),
    "SteamAPI_ISteamNetworkingUtils_IsFakeIPv4": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetIPv4FakeIPType": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetRealIdentityForFakeIP": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.POINTER(structs.SteamNetworkingIdentity),
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int, typedefs.int32),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_float),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueString": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValuePtr": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, ctypes.c_int, typedefs.int32),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, ctypes.c_int, ctypes.c_float),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueString": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.HSteamNetConnection, ctypes.c_int, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.FnSteamNetConnectionStatusChanged),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.FnSteamNetAuthenticationStatusChanged),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.FnSteamRelayNetworkStatusChanged),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.FnSteamNetworkingFakeIPResult),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.FnSteamNetworkingMessagesSessionRequest),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.FnSteamNetworkingMessagesSessionFailed),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetConfigValue": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_ssize_t,
            ctypes.c_int,
            ctypes.c_void_p,
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_SetConfigValueStruct": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingConfigValue_t),
            ctypes.c_int,
            ctypes.c_ssize_t,
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetConfigValue": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_ssize_t,
            ctypes.POINTER(ctypes.c_int),
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_size_t),
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_GetConfigValueInfo": (
        ctypes.c_char_p,
        (ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)),
    ),
    "SteamAPI_ISteamNetworkingUtils_IterateGenericEditableConfigValues": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_int, ctypes.c_bool),
    ),
    "SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString": (
        None,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIPAddr), ctypes.c_char_p),
    ),
    "SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIPAddr)),
    ),
    "SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ToString": (
        None,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.c_char_p,
            typedefs.uint32,
        ),
    ),
    "SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_char_p),
    ),
    "SteamAPI_SteamGameServer_v015": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamGameServer_SetProduct": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetGameDescription": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetModDir": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetDedicatedServer": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamGameServer_LogOn": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_LogOnAnonymous": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_LogOff": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_BLoggedOn": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_BSecure": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_GetSteamID": (typedefs.uint64_steamid, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_WasRestartRequested": (ctypes.c_bool, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_SetMaxPlayerCount": (None, (ctypes.c_void_p, ctypes.c_int)),
    "SteamAPI_ISteamGameServer_SetBotPlayerCount": (None, (ctypes.c_void_p, ctypes.c_int)),
    "SteamAPI_ISteamGameServer_SetServerName": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetMapName": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetPasswordProtected": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamGameServer_SetSpectatorPort": (None, (ctypes.c_void_p, typedefs.uint16)),
    "SteamAPI_ISteamGameServer_SetSpectatorServerName": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_ClearAllKeyValues": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_SetKeyValue": (
        None,
        (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamGameServer_SetGameTags": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetGameData": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetRegion": (None, (ctypes.c_void_p, ctypes.c_char_p)),
    "SteamAPI_ISteamGameServer_SetAdvertiseServerActive": (None, (ctypes.c_void_p, ctypes.c_bool)),
    "SteamAPI_ISteamGameServer_GetAuthSessionTicket": (
        typedefs.HAuthTicket,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(structs.SteamNetworkingIdentity),
        ),
    ),
    "SteamAPI_ISteamGameServer_BeginAuthSession": (
        ctypes.c_int,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamGameServer_EndAuthSession": (None, (ctypes.c_void_p, typedefs.uint64_steamid)),
    "SteamAPI_ISteamGameServer_CancelAuthTicket": (None, (ctypes.c_void_p, typedefs.HAuthTicket)),
    "SteamAPI_ISteamGameServer_UserHasLicenseForApp": (
        ctypes.c_int,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.AppId_t),
    ),
    "SteamAPI_ISteamGameServer_RequestUserGroupStatus": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamGameServer_GetGameplayStats": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_GetServerReputation": (typedefs.SteamAPICall_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_GetPublicIP": (structs.SteamIPAddress_t, (ctypes.c_void_p,)),
    "SteamAPI_ISteamGameServer_HandleIncomingPacket": (
        ctypes.c_bool,
        (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, typedefs.uint32, typedefs.uint16),
    ),
    "SteamAPI_ISteamGameServer_GetNextOutgoingPacket": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.POINTER(typedefs.uint32),
            ctypes.POINTER(typedefs.uint16),
        ),
    ),
    "SteamAPI_ISteamGameServer_AssociateWithClan": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamGameServer_ComputeNewPlayerCompatibility": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.POINTER(structs.CSteamID),
        ),
    ),
    "SteamAPI_ISteamGameServer_CreateUnauthenticatedUserConnection": (
        typedefs.uint64_steamid,
        (ctypes.c_void_p,),
    ),
    "SteamAPI_ISteamGameServer_SendUserDisconnect_DEPRECATED": (
        None,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamGameServer_BUpdateUserData": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_SteamGameServerStats_v001": (ctypes.c_void_p, ()),
    "SteamAPI_ISteamGameServerStats_RequestUserStats": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamGameServerStats_GetUserStatInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.POINTER(typedefs.int32)),
    ),
    "SteamAPI_ISteamGameServerStats_GetUserStatFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.POINTER(ctypes.c_float)),
    ),
    "SteamAPI_ISteamGameServerStats_GetUserAchievement": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)),
    ),
    "SteamAPI_ISteamGameServerStats_SetUserStatInt32": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, typedefs.int32),
    ),
    "SteamAPI_ISteamGameServerStats_SetUserStatFloat": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p, ctypes.c_float),
    ),
    "SteamAPI_ISteamGameServerStats_UpdateUserAvgRateStat": (
        ctypes.c_bool,
        (
            ctypes.c_void_p,
            typedefs.uint64_steamid,
            ctypes.c_char_p,
            ctypes.c_float,
            ctypes.c_double,
        ),
    ),
    "SteamAPI_ISteamGameServerStats_SetUserAchievement": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamGameServerStats_ClearUserAchievement": (
        ctypes.c_bool,
        (ctypes.c_void_p, typedefs.uint64_steamid, ctypes.c_char_p),
    ),
    "SteamAPI_ISteamGameServerStats_StoreUserStats": (
        typedefs.SteamAPICall_t,
        (ctypes.c_void_p, typedefs.uint64_steamid),
    ),
    "SteamAPI_ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort": (None, (ctypes.c_void_p,)),
    "SteamAPI_ISteamNetworkingFakeUDPPort_SendMessageToFakeIP": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.c_void_p,
            typedefs.uint32,
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingFakeUDPPort_ReceiveMessages": (
        ctypes.c_int,
        (
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.POINTER(structs.SteamNetworkingMessage_t)),
            ctypes.c_int,
        ),
    ),
    "SteamAPI_ISteamNetworkingFakeUDPPort_ScheduleCleanup": (
        None,
        (ctypes.c_void_p, ctypes.POINTER(structs.SteamNetworkingIPAddr)),
    ),
    "SteamAPI_SteamIPAddress_t_IsSet": (ctypes.c_bool, (ctypes.POINTER(structs.SteamIPAddress_t),)),
    "SteamAPI_MatchMakingKeyValuePair_t_Construct": (
        None,
        (ctypes.POINTER(structs.MatchMakingKeyValuePair_t),),
    ),
    "SteamAPI_servernetadr_t_Construct": (None, (ctypes.POINTER(structs.servernetadr_t),)),
    "SteamAPI_servernetadr_t_Init": (
        None,
        (ctypes.POINTER(structs.servernetadr_t), ctypes.c_uint, typedefs.uint16, typedefs.uint16),
    ),
    "SteamAPI_servernetadr_t_GetQueryPort": (
        typedefs.uint16,
        (ctypes.POINTER(structs.servernetadr_t),),
    ),
    "SteamAPI_servernetadr_t_SetQueryPort": (
        None,
        (ctypes.POINTER(structs.servernetadr_t), typedefs.uint16),
    ),
    "SteamAPI_servernetadr_t_GetConnectionPort": (
        typedefs.uint16,
        (ctypes.POINTER(structs.servernetadr_t),),
    ),
    "SteamAPI_servernetadr_t_SetConnectionPort": (
        None,
        (ctypes.POINTER(structs.servernetadr_t), typedefs.uint16),
    ),
    "SteamAPI_servernetadr_t_GetIP": (typedefs.uint32, (ctypes.POINTER(structs.servernetadr_t),)),
    "SteamAPI_servernetadr_t_SetIP": (
        None,
        (ctypes.POINTER(structs.servernetadr_t), typedefs.uint32),
    ),
    "SteamAPI_servernetadr_t_GetConnectionAddressString": (
        ctypes.c_char_p,
        (ctypes.POINTER(structs.servernetadr_t),),
    ),
    "SteamAPI_servernetadr_t_GetQueryAddressString": (
        ctypes.c_char_p,
        (ctypes.POINTER(structs.servernetadr_t),),
    ),
    "SteamAPI_servernetadr_t_IsLessThan": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.servernetadr_t), ctypes.POINTER(structs.servernetadr_t)),
    ),
    "SteamAPI_servernetadr_t_Assign": (
        None,
        (ctypes.POINTER(structs.servernetadr_t), ctypes.POINTER(structs.servernetadr_t)),
    ),
    "SteamAPI_servernetadr_t_IsEqualTo": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.servernetadr_t), ctypes.POINTER(structs.servernetadr_t)),
    ),
    "SteamAPI_gameserveritem_t_Construct": (None, (ctypes.POINTER(structs.gameserveritem_t),)),
    "SteamAPI_gameserveritem_t_GetName": (
        ctypes.c_char_p,
        (ctypes.POINTER(structs.gameserveritem_t),),
    ),
    "SteamAPI_gameserveritem_t_SetName": (
        None,
        (ctypes.POINTER(structs.gameserveritem_t), ctypes.c_char_p),
    ),
    "SteamAPI_gameserveritem_t_IsEqualTo": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.gameserveritem_t), ctypes.POINTER(structs.gameserveritem_t)),
    ),
    "SteamAPI_SteamNetworkingIPAddr_Clear": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIPAddr_IsIPv6AllZeros": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIPAddr_SetIPv6": (
        None,
        (
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.POINTER(typedefs.uint8),
            typedefs.uint16,
        ),
    ),
    "SteamAPI_SteamNetworkingIPAddr_SetIPv4": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr), typedefs.uint32, typedefs.uint16),
    ),
    "SteamAPI_SteamNetworkingIPAddr_IsIPv4": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIPAddr_GetIPv4": (
        typedefs.uint32,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIPAddr_SetIPv6LocalHost": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr), typedefs.uint16),
    ),
    "SteamAPI_SteamNetworkingIPAddr_IsLocalHost": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIPAddr_ToString": (
        None,
        (
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.c_char_p,
            typedefs.uint32,
            ctypes.c_bool,
        ),
    ),
    "SteamAPI_SteamNetworkingIPAddr_ParseString": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr), ctypes.c_char_p),
    ),
    "SteamAPI_SteamNetworkingIPAddr_IsEqualTo": (
        ctypes.c_bool,
        (
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
        ),
    ),
    "SteamAPI_SteamNetworkingIPAddr_GetFakeIPType": (
        ctypes.c_int,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIPAddr_IsFakeIP": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIPAddr),),
    ),
    "SteamAPI_SteamNetworkingIdentity_Clear": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_IsInvalid": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetSteamID": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), typedefs.uint64_steamid),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetSteamID": (
        typedefs.uint64_steamid,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetSteamID64": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), typedefs.uint64),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetSteamID64": (
        typedefs.uint64,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetXboxPairwiseID": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_char_p),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetXboxPairwiseID": (
        ctypes.c_char_p,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetPSNID": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), typedefs.uint64),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetPSNID": (
        typedefs.uint64,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetIPAddr": (
        None,
        (
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.POINTER(structs.SteamNetworkingIPAddr),
        ),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetIPAddr": (
        ctypes.POINTER(structs.SteamNetworkingIPAddr),
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetIPv4Addr": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), typedefs.uint32, typedefs.uint16),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetIPv4": (
        typedefs.uint32,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetFakeIPType": (
        ctypes.c_int,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_IsFakeIP": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetLocalHost": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_IsLocalHost": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetGenericString": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_char_p),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetGenericString": (
        ctypes.c_char_p,
        (ctypes.POINTER(structs.SteamNetworkingIdentity),),
    ),
    "SteamAPI_SteamNetworkingIdentity_SetGenericBytes": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_void_p, typedefs.uint32),
    ),
    "SteamAPI_SteamNetworkingIdentity_GetGenericBytes": (
        ctypes.POINTER(typedefs.uint8),
        (ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.POINTER(ctypes.c_int)),
    ),
    "SteamAPI_SteamNetworkingIdentity_IsEqualTo": (
        ctypes.c_bool,
        (
            ctypes.POINTER(structs.SteamNetworkingIdentity),
            ctypes.POINTER(structs.SteamNetworkingIdentity),
        ),
    ),
    "SteamAPI_SteamNetworkingIdentity_ToString": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_char_p, typedefs.uint32),
    ),
    "SteamAPI_SteamNetworkingIdentity_ParseString": (
        ctypes.c_bool,
        (ctypes.POINTER(structs.SteamNetworkingIdentity), ctypes.c_char_p),
    ),
    "SteamAPI_SteamNetworkingMessage_t_Release": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingMessage_t),),
    ),
    "SteamAPI_SteamNetworkingConfigValue_t_SetInt32": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingConfigValue_t), ctypes.c_int, ctypes.c_int32),
    ),
    "SteamAPI_SteamNetworkingConfigValue_t_SetInt64": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingConfigValue_t), ctypes.c_int, ctypes.c_int64),
    ),
    "SteamAPI_SteamNetworkingConfigValue_t_SetFloat": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingConfigValue_t), ctypes.c_int, ctypes.c_float),
    ),
    "SteamAPI_SteamNetworkingConfigValue_t_SetPtr": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingConfigValue_t), ctypes.c_int, ctypes.c_void_p),
    ),
    "SteamAPI_SteamNetworkingConfigValue_t_SetString": (
        None,
        (ctypes.POINTER(structs.SteamNetworkingConfigValue_t), ctypes.c_int, ctypes.c_char_p),
    ),
    "SteamAPI_SteamDatagramHostedAddress_Clear": (
        None,
        (ctypes.POINTER(structs.SteamDatagramHostedAddress),),
    ),
    "SteamAPI_SteamDatagramHostedAddress_GetPopID": (
        typedefs.SteamNetworkingPOPID,
        (ctypes.POINTER(structs.SteamDatagramHostedAddress),),
    ),
    "SteamAPI_SteamDatagramHostedAddress_SetDevAddress": (
        None,
        (
            ctypes.POINTER(structs.SteamDatagramHostedAddress),
            typedefs.uint32,
            typedefs.uint16,
            typedefs.SteamNetworkingPOPID,
        ),
    ),
}
# The accessor of each interface by kind: user, gameserver or global.
ACCESSORS: Final[Mapping[str, Mapping[str, str]]] = {
    "ISteamApps": {"user": "SteamAPI_SteamApps_v009"},
    "ISteamController": {"user": "SteamAPI_SteamController_v008"},
    "ISteamFriends": {"user": "SteamAPI_SteamFriends_v018"},
    "ISteamGameServer": {"gameserver": "SteamAPI_SteamGameServer_v015"},
    "ISteamGameServerStats": {"gameserver": "SteamAPI_SteamGameServerStats_v001"},
    "ISteamHTMLSurface": {"user": "SteamAPI_SteamHTMLSurface_v005"},
    "ISteamHTTP": {
        "gameserver": "SteamAPI_SteamGameServerHTTP_v003",
        "user": "SteamAPI_SteamHTTP_v003",
    },
    "ISteamInput": {"user": "SteamAPI_SteamInput_v007"},
    "ISteamInventory": {
        "gameserver": "SteamAPI_SteamGameServerInventory_v003",
        "user": "SteamAPI_SteamInventory_v003",
    },
    "ISteamMatchmaking": {"user": "SteamAPI_SteamMatchmaking_v009"},
    "ISteamMatchmakingServers": {"user": "SteamAPI_SteamMatchmakingServers_v003"},
    "ISteamMusic": {"user": "SteamAPI_SteamMusic_v001"},
    "ISteamNetworking": {
        "gameserver": "SteamAPI_SteamGameServerNetworking_v006",
        "user": "SteamAPI_SteamNetworking_v006",
    },
    "ISteamNetworkingMessages": {
        "gameserver": "SteamAPI_SteamGameServerNetworkingMessages_SteamAPI_v002",
        "user": "SteamAPI_SteamNetworkingMessages_SteamAPI_v002",
    },
    "ISteamNetworkingSockets": {
        "gameserver": "SteamAPI_SteamGameServerNetworkingSockets_SteamAPI_v013",
        "user": "SteamAPI_SteamNetworkingSockets_SteamAPI_v013",
    },
    "ISteamNetworkingUtils": {"global": "SteamAPI_SteamNetworkingUtils_SteamAPI_v004"},
    "ISteamParentalSettings": {"user": "SteamAPI_SteamParentalSettings_v001"},
    "ISteamParties": {"user": "SteamAPI_SteamParties_v002"},
    "ISteamRemotePlay": {"user": "SteamAPI_SteamRemotePlay_v004"},
    "ISteamRemoteStorage": {"user": "SteamAPI_SteamRemoteStorage_v016"},
    "ISteamScreenshots": {"user": "SteamAPI_SteamScreenshots_v003"},
    "ISteamTimeline": {"user": "SteamAPI_SteamTimeline_v004"},
    "ISteamUGC": {
        "gameserver": "SteamAPI_SteamGameServerUGC_v021",
        "user": "SteamAPI_SteamUGC_v021",
    },
    "ISteamUser": {"user": "SteamAPI_SteamUser_v023"},
    "ISteamUserStats": {"user": "SteamAPI_SteamUserStats_v013"},
    "ISteamUtils": {
        "gameserver": "SteamAPI_SteamGameServerUtils_v011",
        "user": "SteamAPI_SteamUtils_v011",
    },
    "ISteamVideo": {"user": "SteamAPI_SteamVideo_v007"},
}
