
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
import random
import os
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import BR_IMDB_TEMPLATE, PROTECT_CONTENT, AUTH_CHANNEL, BATCH_LINK, ADMINS
from utils import get_poster



import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from info import IMDB









Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

ALL_PIC = [
 "https://telegra.ph/file/d6693066f82ed4079c528.jpg",
 "https://telegra.ph/file/65a9972e351b02640d0f4.jpg"
 ]



START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>

"""














@Client.on_message(filters.reply)             
async def start_message(client, message):    
    searchh = message.text 
# @Client.on_message(filters.private & filters.forwarded)
# async def start_message(client, message):           
    imdb = await get_poster(searchh) if IMDB else None
    

    if imdb:

        cap = BR_IMDB_TEMPLATE.format(
        query=searchh,
        title=imdb['title'],
        votes=imdb['votes'],
        aka=imdb["aka"],
        seasons=imdb["seasons"],
        box_office=imdb['box_office'],
        localized_title=imdb['localized_title'],
        kind=imdb['kind'],
        imdb_id=imdb["imdb_id"],
        cast=imdb["cast"],
        runtime=imdb["runtime"],
        countries=imdb["countries"],
        certificates=imdb["certificates"],
        languages=imdb["languages"],
        director=imdb["director"],
        writer=imdb["writer"],
        producer=imdb["producer"],
        composer=imdb["composer"],
        cinematographer=imdb["cinematographer"],
        music_team=imdb["music_team"],
        distributors=imdb["distributors"],
        release_date=imdb['release_date'],
        year=imdb['year'],
        genres=imdb['genres'],
        poster=imdb['poster'],
        plot=imdb['plot'],
        rating=imdb['rating'],
        url=imdb['url'],
        **locals()

    )                           
    if imdb and imdb.get('poster'):
        try:
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('𝐋𝐞𝐭𝐞𝐬𝐭 𝐓𝐫𝐲', url='http://t.me/nasrani_update')      
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_photo(photo=imdb.get('poster'), caption=cap,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
                                      
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('𝐋𝐞𝐭𝐞𝐬𝐭 𝐓𝐫𝐲', url='http://t.me/nasrani_update')           
            ]]
            hmm = await message.reply_photo(photo=poster, caption=cap,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
        except Exception as e:
            logger.exception(e)
