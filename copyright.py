from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
# -------------------------------------------------------------------------------------

BOT_USERNAME = os.environ.get("BOT_USERNAME","ShelbyXcopyright_bot")

OWNER_ID = "6392704171"
# -------------------------------------------------------------------------------------

API_ID = "27202551"
API_HASH = "e070ca5c168293a0a4b3f19e3eeb2855"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖 ˹ Sʜᴇʟʙʏ ꭙ Cᴏᴘʏʀɪɢʜᴛ ˼  🛡️ </b>

𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 ˹ Sʜᴇʟʙʏ ꭙ Cᴏᴘʏʀɪɢʜᴛ ˼, Pʀᴏᴛᴇᴄᴛᴏʀ ᴏғ Sʜᴇʟʙʏ 🗿🗿🤝ᴅᴏ ʏᴏᴜ ᴛʜɪɴᴋ ᴛʜᴀᴛ ʏᴏᴜ ᴡɪʟʟ ᴋɪʟʟ Sʜᴇʟʙʏ? ɪᴛ ɪs ɴᴏᴛ ᴘᴏssɪʙʟᴇ ʙᴇᴄᴀᴜsᴇ ʜᴇʀᴇ I ᴀᴍ, 
ᴛʜᴇ ᴅʀᴇᴀᴍ ᴏғ ᴋɪʟʟɪɴɢ Sʜᴇʟʙʏ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ᴀ ᴅʀᴇᴀᴍ.🤣

Nʜɪ Hᴏɢᴀ Tᴜᴍsᴇ Cᴏᴘʏʀɪɢʜᴛ Dᴏɢᴇ? ᴄʜᴀʟᴏ Dᴏ

Sᴜᴘᴘᴏʀᴛ :- @TheShelbyEmpire """

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="dil_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/b8a9e5bf39b09b3bac4e3.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/ShelbyEmpireNetwork"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links_and_keywords(client, message):
    keywords = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]
    
    if any(keyword.lower() in message.text.lower() for keyword in keywords) or any(link in message.text.lower() for link in ["http", "https", "www."]):
        await message.delete()
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    try:
        if len(message.text.split()) >= 10:

       
            print(f"Deleted message from {message.from_user.username}: {message.text}")
            
            
            await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
        
        
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪║┏━━━━━━➣║┣⪼ ᴏᴡɴᴇʀ :- @sigma_madaraa ║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ShelbyEmpireNetwork║┗━━━━━━➣║╔═════ஜ۩۞۩ஜ════╗║अनंत अखंड अमर अविनाशी║कष्ट हरण है║शंभु कैलाशी║╚═════ஜ۩۞۩ஜ════╝╚═════════════════❍⊱❁ """)
app.run()
