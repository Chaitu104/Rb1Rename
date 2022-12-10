"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/rb1bots
Repo Link : https://github.com/sarthakkale16/Rb1Rename
License Link : https://github.com/sarthakkale16/Rb1Rename/blob/main/LICENSE
"""

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)           
    txt=f"★ ʜᴇʏ {user.mention}  \n\n sᴇɴᴅ ᴍᴇ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴛᴏ ʀᴇɴᴀᴍᴇ ! \n𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 @rb1bots"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("★ ᴅᴇᴠᴇʟᴏᴘᴇʀ ★", callback_data='dev')
        ],[
        InlineKeyboardButton('✘ ᴜᴘᴅᴀᴛᴇs ✘', url='https://t.me/rb1bots'),
        InlineKeyboardButton('✘ sᴜᴘᴘᴏʀᴛ ✘', url='https://t.me/requestbox1')
        ],[
        InlineKeyboardButton('✘ ᴀʙᴏᴜᴛ ✘', callback_data='about'),
        InlineKeyboardButton('✘ ʜᴇʟᴘ ✘', callback_data='help')
        ],[
        InlineKeyboardButton("✘ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs ✘", url='https://t.me/requestbox1official')
        ],[
        InlineKeyboardButton("✘ ᴏᴜʀ ᴍᴏᴠɪᴇ ʙᴏᴛ ✘", url='https://t.me/rb1filter3_bot')
        ],[
        InlineKeyboardButton("ɢɪᴛʜᴜʙ ғᴏʀᴋs", url='https://github.com/sarthakkale16')
        ],[
        InlineKeyboardButton("ᴍᴏᴠɪᴇs ᴀᴠᴀɪʟᴀʙʟᴇ ?", url='https://t.me/rb1index'),
        InlineKeyboardButton("★ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ★", url='https://t.me/rb1official')
        ]
        ])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""★ ʜᴇʏ {query.from_user.mention} \n\n sᴇɴᴅ ᴍᴇ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴛᴏ ʀᴇɴᴀᴍᴇ ! \n𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 @rb1bots !""",
            reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", callback_data='dev')
        ],[
        InlineKeyboardButton('✘ ᴜᴘᴅᴀᴛᴇs ✘', url='https://t.me/rb1bots'),
        InlineKeyboardButton('✘ sᴜᴘᴘᴏʀᴛ ✘', url='https://t.me/requestbox1')
        ],[
        InlineKeyboardButton('✘ ᴀʙᴏᴜᴛ ✘', callback_data='about'),
        InlineKeyboardButton('✘ ʜᴇʟᴘ ✘', callback_data='help')
        ],[
        InlineKeyboardButton("✘ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs ✘", url='https://t.me/requestbox1official')
        ],[
        InlineKeyboardButton("✘ ᴏᴜʀ ᴍᴏᴠɪᴇ ʙᴏᴛ ✘", url='https://t.me/rb1filter3_bot')
        ],[
        InlineKeyboardButton("✘ ɢɪᴛʜᴜʙ ғᴏʀᴋs ✘", url='https://www.github.com/sarthakxd16')
        ],[
        InlineKeyboardButton("✘ ғɪʟᴇs ᴀᴠᴀɪʟᴀʙʟᴇ ✘", url='https://t.me/rb1index'),
        InlineKeyboardButton("✘ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ✘", url='https://t.me/rb1official')
        ]
        ]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ Do Not change source code & source link ⚠️ #
               InlineKeyboardButton("★ ᴅᴇᴠᴇʟᴏᴘᴇʀ ★", url="https://t.me/know_sarthak16")
               ],[
               InlineKeyboardButton("☆ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ☆", url='https://t.me/rb1official')
               ],[
               InlineKeyboardButton("☆ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs ☆", url="https://t.me/rb1bot")
               ],[
               InlineKeyboardButton("★ ᴄʟᴏsᴇ ★", callback_data = "close"),
               InlineKeyboardButton("★ ʜᴏᴍᴇ ★", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✘", url="https://t.me/know_sarthak16")
               ],[
               InlineKeyboardButton("☆ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ☆", url='https://t.me/rb1official')
               ],[
                InlineKeyboardButton("☆ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs ☆", url="https://t.me/rb1bots")
               ],[
               InlineKeyboardButton("★ ᴄʟᴏsᴇ ★", callback_data = "close"),
               InlineKeyboardButton("★ ʜᴏᴍᴇ ★", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✘", url="https://t.me/know_sarthak16")
               ],[
               InlineKeyboardButton("☆ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ☆", url='https://t.me/rb1official')
               ],[
                InlineKeyboardButton("☆ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs ☆", url="https://t.me/requestbox1official")
               ],[
               InlineKeyboardButton("★ ᴄʟᴏsᴇ ★", callback_data = "close"),
               InlineKeyboardButton("★ ʜᴏᴍᴇ ★", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





