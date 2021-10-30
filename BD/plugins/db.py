from pymongo import MongoClient
from BD import DB_URL, BOT_ID, tbot, LOG_SPAM
from telethon.sync import events
db = MongoClient(DB_URL)
db = db["botto"]

@tbot.on(events.ChatAction(func=lambda e: e.user_added and e.user_id == BOT_ID))
async def ok(e):
     x = db.chats.find_one({"id": 1})
     ids = x["ids"] if x else []
     ids.append(e.chat.id)
     db.chats.update_one({"id": 1}, {"$set": {"ids": ids}}, upsert=True)
     await tbot.send_message(LOG_SPAM, f"I've been added to {(e.chat.id)}")
