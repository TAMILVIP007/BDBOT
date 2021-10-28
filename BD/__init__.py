from telethon import TelegramClient
from config import *
import logging
import time
import os


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

DEVS= {int(x) for x in os.environ.get("DEVS", "").split()}
GC_ID = os.environ.get("GC_ID", None)
CH_ID = os.environ.get("CH_ID", None)
LOG_SPAM = os.environ.get("LOG_SPAM", None)
SUPPORT = os.environ.get("SUPPORT", None)
CHANNEL = os.environ.get("CHANNEL", None)

tbot = TelegramClient('botto', API_KEY, API_HASH).start(bot_token=TOKEN)
