from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["listbot", "bot"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention},

felin bot list ✧✧✦
Manage Bot »
@skytrixszbot
Menfess »
@skytrixszrobot
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("♡¸.•* Owner", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "Support *•.¸♡",
                        url="t.me/wibuhouse",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "List Bot"
