from telethon import TelegramClient
from config import *
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

DRVS= {int(x) for x in os.environ.get("DEVS", "").split()}

tbot = TelegramClient('botto', API_KEY, API_HASH).start(bot_token=TOKEN)
