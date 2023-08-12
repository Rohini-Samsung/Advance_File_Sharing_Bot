from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> 1. Hoi 💀, First Join the channel \n 2. Tap on Original link again or Reload ⚡ \n 3. Tap on Start and Done ✅ </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton("🤷🏻‍♀️ Close", callback_data = "close") ],
                    [ InlineKeyboardButton("💁🏻‍♀️ Report Error Directly", callback_data = "help") ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try: 
            await query.message.reply_to_message.delete() 
        except: 
            pass
    elif data == "help":
        await query.message.edit_text(
            text = f"<b> 🙍🏻‍♀️Damn ! Sorry for trouble 🙆🏻‍♀️ \n Contact our Support team at <a href='https://t.me/+u91inEU1hvcwMDY1'>Click Here</a> ⚡</b>",
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton("🙍🏻‍♀️ ᴄʟᴏsᴇ", callback_data = "close") ]
                ]
            )
        )
