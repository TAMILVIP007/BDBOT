from BD import tbot, GC_ID, CH_ID
from telethon.sync import events

@tbot.on(events.NewMessage(incoming=True))
async def x(e):
 if e.chat.id == 1686303934 and e.sender.id == 1602095999:
  try:
    ids = db.chats.find_one({"id": 1})["ids"]
    for x in ids:
        await e.forward_to(x)
  except Exception as f:
        await e.reply(f'Error {f}')
