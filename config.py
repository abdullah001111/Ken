# Codexbotz # @mrismanaziz

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", "27382214"))
API_HASH = os.environ.get("API_HASH", "6a3913eb3f026ab02e7ac1c420df2ad0")

CHANNEL_DB = int(os.environ.get("CHANNEL_DB", "-1001982189344"))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ken:ken@cluster0.4dbw2ui.mongodb.net/?retryWrites=true&w=majority")

RESTRICT = strtobool(os.environ.get("RESTRICT", "True"))

FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1001564901630"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1001927957401"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "-1001930063761"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "-1001977636876"))

WORKERS = int(os.environ.get("WORKERS", "4"))

START_MESSAGE = os.environ.get(
    "START_MESSAGE",
    "Hello {mention}👋"
    "\n\n"
    "I am  a file store bot for @anime_channelz, please join the channel to use me.",
)
FORCE_MESSAGE = os.environ.get(
    "FORCE_MESSAGE",
    "Sᴏʀʀy Dᴜᴅᴇ, Seems Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😁. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ to use me."
    "\n\n"
)

try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split(5984303934 1690217497 6672416716))]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")
    
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
DISABLE_BUTTON = strtobool(os.environ.get("DISABLE_BUTTON", "False"))


LOGS_FILE = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOGS_FILE, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
