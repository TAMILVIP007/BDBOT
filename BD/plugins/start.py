from BD import tbot
from telethon.sync import events
from BD import SUPPORT, CHANNEL
from telethon import Button


@tbot.on(events.NewMessage(pattern="[/!]start"))
async def lol(event):
  await tbot.send_message(event.chat_id, f'__Hey {(event.sender.first_name)}.\n I am a forwader bot made for k__.')