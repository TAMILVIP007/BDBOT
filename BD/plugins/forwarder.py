from BD import tbot, GC_ID, CH_ID
from telethon.sync import events

@tbot.on(events.NewMessage(incoming=True))
async def x(e):
 if e.chat.id == GC_ID and e.sender.id == CH_ID:
  try:
    for x in [-1001176306346, -1001443691244]:
        await e.forward_to(x)
  except Exception as f:
        await event.reply(f'Error {f}')
