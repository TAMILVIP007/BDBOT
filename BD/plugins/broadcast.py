from telethon.sync import events
from BD import DEVS, tbot

@tbot.on(events.NewMessage(pattern="[/!]bcast"))
async def lmoa(event):
   if event.sender.id in DEVS:
      try:
         for y in [-1001176306346, -1001686303934]:
             x = await event.get_reply_message()
             await tbot.send_message(y,x)
             await event.reply('**Successfully Braodcasted**')
      except Exception as lol:
             await event.client.send_message(-1001602095999, f'Error {lol}')
