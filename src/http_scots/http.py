"""The Scots HTTPMethod and HTTPStatus enums."""

from enum import IntEnum, StrEnum

__all__ = ["HTTPMethod", "HTTPStatus"]


class HTTPStatus(IntEnum):
    """HTTP status codes and reason phrases

    Status codes from the following RFCs are all observed:

        * RFC 9110: HTTP Semantics, obsoletes 7231, which obsoleted 2616
        * RFC 6585: Additional HTTP Status Codes
        * RFC 3229: Delta encoding in HTTP
        * RFC 4918: HTTP Extensions for WebDAV, obsoletes 2518
        * RFC 5842: Binding Extensions to WebDAV
        * RFC 7238: Permanent Redirect
        * RFC 2295: Transparent Content Negotiation in HTTP
        * RFC 2774: An HTTP Extension Framework
        * RFC 7725: An HTTP Status Code to Report Legal Obstacles
        * RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2)
        * RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)
        * RFC 8297: An HTTP Status Code for Indicating Hints
        * RFC 8470: Using Early Data in HTTP
    """

    def __new__(cls, value, phrase, description=""):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.phrase = phrase  # type: ignore[attr-defined]
        obj.description = description  # type: ignore[attr-defined]
        return obj

    @property
    def is_informational(self):
        return 100 <= self <= 199

    @property
    def is_success(self):
        return 200 <= self <= 299

    @property
    def is_redirection(self):
        return 300 <= self <= 399

    @property
    def is_client_error(self):
        return 400 <= self <= 499

    @property
    def is_server_error(self):
        return 500 <= self <= 599

    # informational
    AYE_ON_YE_GO = (
        100,
        "Aye on ye go",
        "Awright, ah've goat it, keep gaun, big man.",
    )
    RIGHT_WERE_SWAPPIN = (
        101,
        "Right were swappin",
        "Right, we're daein it a DIFFERENT wey noo, dae whit the Upgrade heider says, ya bam.",
    )
    AYE_HAUD_ON = (
        102,
        "Aye haud on",
        "Haud yer horses, am still workin' oan it.",
    )
    HERES_A_WEE_CLUE = (
        103,
        "Heres a wee clue",
        "Here's a wee heads-up afore the main even', hen.",
    )

    # success
    NAE_BOTHER = (
        200,
        "Nae bother",
        "There ye go, sorted, here's yer paper.",
    )
    THATS_IT_MADE = (
        201,
        "Thats it made",
        "Made yer new ting, the URL's in the Location heider, there ye go.",
    )
    AYE_AHLL_SEE_TAE_IT = (
        202,
        "Aye ahll see tae it",
        "Aye awright, ah'll get tae it... eventually. Doon the line, like.",
    )
    DINNAE_QUOTE_ME = (
        203,
        "Dinnae quote me",
        "This is second-hand, tae, but it'll dae.",
    )
    HEHAW = (
        204,
        "Hehaw",
        "Done. Sent ye nothin' back, get tae fuck... ah mean, aw done, nothin' tae send.",
    )
    CLEAR_THAT_AFF_AN_START_AGAIN = (
        205,
        "Clear that aff an start again",
        "Wipe that, start again, ya muppet.",
    )
    HERES_A_WEE_BIT = (
        206,
        "Heres a wee bit",
        "Here's a wee bit oh it, no the hale ting.",
    )
    BIT_O_THIS_BIT_O_THAT = (
        207,
        "Bit o this bit o that",
        "Awright there's aboot ten dif'rent answers in the hale pile, am no gonnae list them aw here.",
    )
    AH_TELT_YE_AWREADY_YA_WEE_SCUNNER = (
        208,
        "Ah telt ye awready ya wee scunner",
        "Awready telt ye this, ya deaf basturt.",
    )
    HERES_WHITS_CHANGED = (
        226,
        "Heres whits changed",
        "Did it wi' a wee bit oh fancy dif patchin'.",
    )

    # redirection
    TAKE_YER_PICK = (
        300,
        "Take yer pick",
        "There's aboot five dif'rent tings there, pit yer back intae it an' pick wan.",
    )
    WEVE_FLITTED = (
        301,
        "Weve flitted",
        "It's AWAY. Fur good. Follaw the new address, ya roaster.",
    )
    WERE_OWER_THERE_THE_NOO = (
        302,
        "Were ower there the noo",
        "It's owa the road just noo, gae look there.",
    )
    ASK_HIM_OWER_THERE = (
        303,
        "Ask him ower there",
        "Dinnae GET it here, gae look ower there, pal.",
    )
    SAME_AULD_SHITE = (
        304,
        "Same auld shite",
        "Same as last time, take it fae yer cache an' quit whingin'.",
    )
    GO_THROUGH_HIM = (
        305,
        "Go through him",
        "Ye GO THROUGH the middleman, nae arguins.",
    )
    FUCK_OFF_OWER_THERE_FOR_NOO = (
        307,
        "Fuck off ower there for noo",
        "It's doon the road just noo, back efter, dae the same as ye did.",
    )
    FUCK_OFF_OWER_THERE_FOR_GUID = (
        308,
        "Fuck off ower there for guid",
        "Same as 301 but haud the method, ya learned it noo.",
    )

    # client error
    WHIT_THE_FUCKS_THIS = (
        400,
        "Whit the fucks this",
        "Whit in the name oh the wee man am sure ye sent me? Pure pish, that.",
    )
    WHO_THE_FUCK_ARE_YOU = (
        401,
        "Who the fuck are you",
        "Wha the hell ur you? Show me yer papers, hen.",
    )
    GIES_YER_MONEY = (
        402,
        "Gies yer money",
        "Cash up front, big man, nae pleckin' creddit.",
    )
    GET_TAE_FUCK = (
        403,
        "Get tae fuck",
        "Naw. An' nae amount oh beggin's gonnae change ma mind, so it isnae.",
    )
    NO_FUCKIN_HERE_PAL = (
        404,
        "No fuckin here pal",
        "Aint got a scooby, pal. Naebody here by that name.",
    )
    YE_CANNAE_DAE_THAT = (
        405,
        "Ye cannae dae that",
        "Ye cannae dae THAT tae this, ya fanny.",
    )
    WEVE_NANE_O_THAT_KIND = (
        406,
        "Weve nane o that kind",
        "Nah, no in that format, am no a beggar.",
    )
    AN_WHOS_YER_PAL = (
        407,
        "An whos yer pal",
        "The middleman wants tae ken wha you ur first.",
    )
    AHVE_BEEN_STAUNIN_HERE_AGES = (
        408,
        "Ahve been staunin here ages",
        "Too slow, hen. Ah gave up oan ye. Try again.",
    )
    PICK_A_FUCKIN_LANE = (
        409,
        "Pick a fuckin lane",
        "Ye cannae dae that, it'll batter intae somethin' else, ya numpty.",
    )
    DEID_AN_BURIED = (
        410,
        "Deid an buried",
        "It's deid, buried, gone. Quit lookin'.",
    )
    HOW_LANG_IS_IT_THEN = (
        411,
        "How lang is it then",
        "Hoo big is this ting? Tell me, ah'm no a mind reader.",
    )
    THATS_NO_WHIT_WE_AGREED = (
        412,
        "Thats no whit we agreed",
        "Ye said it'd be x first, it's no, so get tae.",
    )
    THATS_FUCKIN_MASSIVE = (
        413,
        "Thats fuckin massive",
        "That's pure muckle, mate. Dinnae shove that here.",
    )
    AHM_NO_READIN_ALL_THAT = (
        414,
        "Ahm no readin all that",
        "That URL's longer than a Glesga scheme, naw.",
    )
    NAE_IDEA_WHIT_THAT_IS = (
        415,
        "Nae idea whit that is",
        "Am no dealin' wi' that format, ya troglodyte.",
    )
    IT_DISNAE_GO_THAT_FAR = (
        416,
        "It disnae go that far",
        "Ye asked fur bits that dinnae even EXIST. Away.",
    )
    AYE_YE_WISH = (
        417,
        "Aye ye wish",
        "Ye expected too much, hen. Disappointed.",
    )
    AHM_A_FUCKIN_TEAPOT = (
        418,
        "Ahm a fuckin teapot",
        "Am a FUKIN TEAPOT, pal. Nae coffee. Away an' boil yer ain kettle.",
    )
    WRONG_CUNT = (
        421,
        "Wrong cunt",
        "That's no fur me, pal. Gae the right server.",
    )
    AH_KEN_WHIT_YE_MEAN_BUT_NAW = (
        422,
        "Ah ken whit ye mean but naw",
        "Ah can read it, but it's utter mince, cannae dae anythin' wi' it.",
    )
    ITS_SNIBBED = (
        423,
        "Its snibbed",
        "Naw, it's locked. Somecunt else's got the key.",
    )
    THE_LAST_WAN_WENT_TITS_UP = (
        424,
        "The last wan went tits up",
        "The bit afore it went tae shit, so this did an' aw.",
    )
    HAUD_YER_HORSES = (
        425,
        "Haud yer horses",
        "Naw, too soon, somecunt could replay that. Dinnae be so keen.",
    )
    GET_YERSEL_A_NEW_WAN = (
        426,
        "Get yersel a new wan",
        "Naw, that auld way? Get wit' the times, upgrade, ya fossil.",
    )
    CHECK_FIRST_YA_CHANCER = (
        428,
        "Check first ya chancer",
        "Put a condition on it first, ya cowboy, or am no touchin' it.",
    )
    SLOW_DOON = (
        429,
        "Slow doon",
        "ALRIGHT. PACK IT IN. Ye've asked aboot a thoosand times. Haud on. Wait yer turn, ya greedy basturt.",
    )
    TOO_MUCH_PISH = (
        431,
        "Too much pish",
        "Yur heiders are pure massive, mate. Trim it doon an' come back.",
    )
    AWAY_YE_CLATTY_WEE_BASTARD = (
        451,
        "Away ye clatty wee bastard",
        "The polis/the lawmental telt me tae take that doon. Naethin' tae dae wi' me, pal.",
    )

    # server errors
    THE_COUNCIL_SAYS_NAW = (
        500,
        "The council says naw",
        "Hell's teeth, ah've gone an' buggered it masel. Am pure scundered.",
    )
    AHVE_FUCKED_IT = (
        501,
        "Ahve fucked it",
        "Naebody taught me how tae dae that. Sorries, pal, I literally cannae.",
    )
    AH_DINNAE_DAE_THAT = (
        502,
        "Ah dinnae dae that",
        "The server ah passed it tae came back wi' pure garbage. Incompetent like.",
    )
    THE_OTHER_BAMPOTS_BROKEN = (
        503,
        "The other bampots broken",
        "Am snowed under, hen. Too many o' yis at once. Come back efter.",
    )
    WERE_FUCKIN_SHUT = (
        504,
        "Were fuckin shut",
        "Ah asked the ither server an' it's just sittin' there like a dummy. Nae answer. Gave up.",
    )
    THE_BASTARDS_NO_ANSWERIN = (
        505,
        "The bastards no answerin",
        "That version? Nah. We dinnae dae that auld pish here.",
    )
    WHIT_FUCKIN_CENTURY_ARE_YE_IN = (
        506,
        "Whit fuckin century are ye in",
        "Config's a pure bombscare, am arguin' wi' masel. Get an admin.",
    )
    AHM_STAPPIT_FU = (
        507,
        "Ahm stappit fu",
        "Am full up, ya animal. Nowheres tae pit any mair oh yer stuff.",
    )
    ROUND_AN_ROUND_YA_DAFT_TWAT = (
        508,
        "Round an round ya daft twat",
        "Ah've went roon in a circle aboot a hunner times. Nipped that in the bud.",
    )
    YELL_NEED_MAIR_THAN_THAT = (
        510,
        "Yell need mair than that",
        "Cannae do that wi'oot ye tellin' me the extra bit. Yer policy, no mine.",
    )
    LOG_IN_TAE_THE_WIFI_PAL = (
        511,
        "Log in tae the wifi pal",
        "Ye need tae sign in tae the wifi first, hen. Nae subscription, nae internet.",
    )


class HTTPMethod(StrEnum):
    """HTTP methods and descriptions

    Methods from the following RFCs are all observed:

        * RFC 9110: HTTP Semantics, obsoletes 7231, which obsoleted 2616
        * RFC 5789: PATCH Method for HTTP
    """

    def __new__(cls, value, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.description = description  # type: ignore[attr-defined]
        return obj

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self._name_}>"

    NIP_IN = "CONNECT", "Let's get the door open tae the server, pal, ah'm comin' in."
    SKIP_IT = "DELETE", "Richt, that's goin' in the skip. Dinnae come lookin' fur it."
    GIES = "GET", "Get me that thing ower there, hen, ah'll no touch it."
    JUST_OOTER = (
        "HEAD",
        "Same as gie's that, but just the label an' the top line. Dinnae bother wi' the body.",
    )
    WHITS_MA_OPTS = (
        "OPTIONS",
        "Gie's a wee list o' whit ye can actually dae here, pal, afore ah embarrass masel.",
    )
    DOABIN = "PATCH", "Just dab a bit here an' there, dinnae rip the hale thing apart."
    HAWDES = (
        "POST",
        "Right, take this bag o' stuff an' dae yer thing wi' it, pal. Yer business, no mine.",
    )
    AWAWI = (
        "PUT",
        "Right, bin the auld yin, this is it noo. The hale replacemint, nae arguin'.",
    )
    ECHAECHO = (
        "TRACE",
        "Right, pass this alang the line an' send it back, ah want tae see wha's been snoopin' oan it.",
    )
