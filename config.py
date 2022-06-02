import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", None)
LOG_CHAT = int(getenv("LOG_CHAT")) 
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", None)
ALIVE_NAME = getenv("ALIVE_NAME", None)
BOT_USERNAME = getenv("BOT_USERNAME", None)
ASSISTANT_NAME = getenv("ASSISTANT_NAME",None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/c5f205198a8f235d2d55b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Koltepol/Koltepol")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/cdb65775448eaa64c87ea.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/cd9da536cbfae1bf1eb56.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/3adda5216e53b355b3ddf.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/6ef95fd3206582e8db84b.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/3cea12ceb8f9a1243e29c.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/45fd06e303ce45ab37d8a.jpg")
YOUTUBE_URL = getenv("YT_URL",https://te.legra.ph/file/c5f205198a8f235d2d55b.jpg")
