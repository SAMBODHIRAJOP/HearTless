
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 😎 ⭐ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 :- ✨ [❛-𝐌𝐫'𝐒𝐦𝐎𝐤𝐞𝐫 🚬 💜](https://t.me/Sanki_Owner)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",
                            url=f"https://t.me/abhijeet_editx")
               ],
               [
                    InlineKeyboardButton(
                            text="𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ❤",
                            url=f"https://t.me/prkboltipublic"),
                            
                    InlineKeyboardButton(
                            text="𝐒𝐭𝐚𝐭𝐮𝐬 🥀",
                            url=f"https://t.me/@Statusforyoubby")
               ],
               [
                        InlineKeyboardButton(
                            text="𝐆𝐫𝐨𝐮𝐩⭐",
                            url=f"https://t.me/Mrabhijeet143")
                   
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("smoker") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝐒𝐦𝐨𝐤𝐞𝐫 💜 𝐌𝐮𝐬𝐢𝐜'𝐗  🚬 𝐎𝐧𝐥𝐢𝐧𝐞 🥀 𝐁𝐨𝐭 𝐎𝐰𝐧𝐞𝐫 :- ✨ [❛-𝐌𝐫'𝐒𝐦𝐎𝐤𝐞𝐫 🚬 💜🐬](https://t.me/sanki_owner)**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❛-𝐌𝐫'𝐒𝐦𝐎𝐤𝐞𝐫 🚬 💜🐬", url="https://t.me/sanki_owner")
                ]
            ]
        )
   )
