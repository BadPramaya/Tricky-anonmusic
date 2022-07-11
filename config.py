from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "16101067"))
API_HASH = getenv("API_HASH", "aeee424293b196381d0cc48cc097daf9")
BOT_TOKEN = getenv("BOT_TOKEN", "none")
BOT_NAME = getenv("BOT_NAME","🎧 MUSIC DOWNLODER BOT 🎵")
BOT_USERNAME = getenv("BOT_USERNAME", "expect_Musicdownloader_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "x_ᴇxᴘᴇʀᴛ_x")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/trxexpertt")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c30b206eae84be444ba45.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c9b7bc377b92cdf03d7c8.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQB2v4aUONKhIK8SHwbR4vXwnJsS2lUYDRmEDMZXT7XRG8i-o8N2_so1Ls6zg_h6oySeADFcym_xzizn1g8yZrlOPjJ8-YEsNcpIVeQ8Dt6xoQ5h9YMnwqGCWr161c2I-irqDwkf2zBfwa2o56ssH8B_eSr-27RHJazsRTxkehVE9oyuBIfKAyDQhRyvKqKxnRSfhPGktukyroGvJ7-d819nFlxVxQpJtM_7QufDvG_PRRbFkMPBmEvBP0KDG4-CCkjSlIBaY2fuGMAz6g88FAhI9nTtBADF9bl4Gn2eibtSyu1U5_FP8ZDMZ6TeEt161AVZZNEL8PGOUCDScZiV8awVAAAAASoTLQIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "94770611075").split()))
