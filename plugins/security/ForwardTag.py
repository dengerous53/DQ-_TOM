import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
import asyncio

@Client.on_message(filters.forwarded & filters.media & filters.group & filters.incoming)
async def channel_tag(bot, message):
    try:
        chat_id = message.chat.id
        forward_msg = await message.copy(chat_id)
        await message.delete()
        await asyncio.sleep(1)
        await forward_msg.delete()
        
    except:
        await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
