from . import *
from telethon.sync import events
from BD import DEVS

@tbot.on(events.NewMessage(pattern="[/!]bcast"))
async def lmoa(event):
   if event.sender.id in DEVS:
      try:
         for y in [-1001176306346, -1001686303934]:
             x = await event.get_reply_message()
             await tbot.send_message(y,x)
      except Exception as lol:
             await event.reply(f'Error {lol}')
