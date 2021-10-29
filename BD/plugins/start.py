from BD import tbot
from telethon.sync import events
from BD import SUPPORT, CHANNEL
from telethon import Button


@tbot.on(events.NewMessage(pattern="[/!]start"))
async def lol(event):
  await tbot.send_message(event.chat_id, f'__Hey {(event.sender.first_name)}.\n I am a forwader bot made for [Channel](t.me/{CHANNEL})__.', file="https://telegra.ph//file/62aa918d3d321651d166d.jpg", buttons=[[Button.url('Support',f't.me/{SUPPORT}'), Button.url('Channel',f't.me/{CHANNEL}')], [Button.inline('Help',data="fk")]])