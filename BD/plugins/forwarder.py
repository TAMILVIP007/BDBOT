from BD import tbot, GC_ID, CH_ID
from telethon.sync import events

@tbot.on(events.NewMessage(incoming=True))
async def x(e):
 if e.chat.id == 1686303934 and e.sender.id == 1602095999:
  try:
    for x in [-1001686303934, -1001176306346]:
        await e.forward_to(x)
  except Exception as f:
        await event.reply(f'Error {f}')
