from telethon.sync import events
from BD import DEVS, tbot
import speedtest

@tbot.on(events.NewMessage(pattern="[/!]bcast"))
async def lmoa(event):
   if event.sender.id in DEVS:
      try:
         for y in [-1001176306346, -1001686303934]:
             x = await event.get_reply_message()
             await tbot.send_message(y,x)
             await event.client.send_message(event.chat_id, '**Successfully Braodcasted**', reply_to=event)
      except Exception as lol:
             await event.client.send_message(-1001686303934, f'Error {lol}')

            
@tbot.on(events.NewMessage(pattern="[/!]speedtest"))
async def test(event):
   if event.sender.id in DEVS:
      try:
          lol=await event.reply('`Processing....`')
          s=speedtest.Speedtest()
          s.download()
          s.upload()
          x=s.results.share()
          await lol.delete()
          await event.respond(file=x)
      except Exception as lmao:
          await event.client.send_message(-1001686303934, f'Error {lmao}')
