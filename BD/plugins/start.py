from BD import tbot
from telethon.sync import events
from BD import SUPPORT, CHANNEL
from telethon import Button


@tbot.on(events.NewMessage(pattern="[/!]start"))
async def lol(event):
  await tbot.send_message(event.chat_id, f'__Hey {(event.sender.first_name)}.\n I am a forwader bot made for {CHANNEL}__.', file="https://telegra.ph//file/62aa918d3d321651d166d.jpg", buttons=[[Button.url('Support',f't.me/{SUPPORT}'),Button.url('Channel',f't.me/{CHANNEL}')],[Button.inline('Help',data="fk")])
  
@tbot.on(events.CallbackQuery(pattern=r"fk"))
async def lmao(event):
  await event.edit('Lol Nothing to describe on help\n\n\n **DEV CMDS**\n `/bcast` To broadcast a msg', button=Button.inline('Back', data='lmao'))

@tbot.on(events.CallbackQuery(pattern=r"lmao"))
async def nigga(event):
   await event.edit(f'__Hey {(event.sender.first_name)}.\n I am a forwader bot made for {CHANNEL}__.', file="https://telegra.ph//file/62aa918d3d321651d166d.jpg", buttons=[[Button.url('Support',f't.me/{SUPPORT}'), Button.url('Channel',f't.me/{CHANNEL}')],[Button.inline('Help',data="fk")])
