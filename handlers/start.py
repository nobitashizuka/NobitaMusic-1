import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        
        ],
     ]
    return buttons
