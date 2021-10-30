from telethon import TelegramClient
from config import *
import logging
import time
import os


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

DEVS= list({int(x) for x in os.environ.get("DEVS", "").split()})
GC_ID = list({int(y) for y in os.environ.get("GC_ID", "").split()})
CH_ID = list({int(z) for z in os.environ.get("GC_ID", "").split()})
LOG_SPAM = os.environ.get("LOG_SPAM", None)
SUPPORT = os.environ.get("SUPPORT", None)
CHANNEL = os.environ.get("CHANNEL", None)
START_IMG = os.environ.get("START_IMG", None)
DB_URL = os.environ.get("DB_URL", None)
BOT_ID = os.environ.get("BOT_ID", None)

tbot = TelegramClient('botto', API_KEY, API_HASH).start(bot_token=TOKEN)
