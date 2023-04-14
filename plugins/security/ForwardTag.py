import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User


@Client.on_message(filters.forwarded & filters.channel & filters.incoming)
async def channel_tag(bot, message):
    try:
        chat_id = message.chat.id
        forward_msg = await message.copy(chat_id)
        await message.delete()
    except:
        await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
