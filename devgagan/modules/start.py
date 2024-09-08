from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import *

# ------------------- Start-Buttons --------------
buttons = [[
        InlineKeyboardButton('✇ Uᴘᴅᴀᴛᴇs ✇', url="https://t.me/HGBOTZ"),
        InlineKeyboardButton('✨BUY PRIMIUM ✨', url="https://t.me/premium_hgbot")
    ],[
        InlineKeyboardButton('〄 Hᴇʟᴘ', url="https://graph.org/vTelegraphBot-09-06-10")
    ]]

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://ibb.co/Wt1n80J",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=InlineKeyboardMarkup(buttons)) 
