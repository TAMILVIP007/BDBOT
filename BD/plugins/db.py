from pymongo import MongoClient
from BD import DB_URL, BOT_ID, tbot, LOG_SPAM
from telethon.sync import events


@tbot.on(events.ChatAction(func=lambda e: e.user_added and e.user_id == BOT_ID))
async def ok(e):
     await tbot.send_message(LOG_SPAM, f"I've been added to {(e.chat.id)}")
