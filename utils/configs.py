import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")


    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", None)

    OWNER_ID = int(os.environ.get("OWNER_ID", "1331793103"))
    BOT_NAME = os.environ.get("BOT_NAME", "ImgBBRexbot")

    START_PIC = "https://telegra.ph/file/93e7ae69a568534628004.jpg"
    HELP_PIC = "https://telegra.ph/file/93e7ae69a568534628004.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @ImgBBRexBot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """
╭────[⚡ ᴀʙᴏᴜᴛ ⚡]───⍟
│
├<b>🤖 𝙱𝚘𝚝 𝙽𝚊𝚖𝚎 : <a href='https://t.me/IMGBBRexBot'>ɪᴍɢʙʙ</a></b>
│
├<b>📢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕  : <a href='https://t.me/Rex_Botz'>ᴊᴏɪɴ</a></b>
│
├<b>👥 𝚅𝚎𝚛𝚜𝚒𝚘𝚗  : <a href='https://t.me/Rex_Bots_Support'>0.9.2ʙᴇᴛᴀ</a></b>
│
├<b>💢 𝚂𝚘𝚞𝚛𝚌𝚎   : <a href='https://github.com/REX-BOTZ/'>ᴅᴇᴘʟᴏʏ</a></b>
│
├<b>🌐 𝚂𝚎𝚛𝚟𝚎𝚛   : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a></b>
│
├<b>📕 𝙻𝚒𝚋𝚛𝚊𝚛𝚢  : <a href='https://github.com/pyrogram'>ᴘʀɢ1.2.8</a></b>
│
├<b>㊙ 𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 : <a href='https://www.python.org'>ᴘʏ3.9.4</a></b>
│
├<b>👨‍💻 𝙳𝚎𝚟      : <a href='https://t.me/BENWOLF24'>ᴡᴏʟғ24</a></b>
│
├<b>🚸 𝙿𝚘𝚠𝚎𝚛𝚎𝚍  : <a href='https://t.me/FluxPlay'>ғʟᴜxᴘʟᴀʏ</a></b>
│
╰──────[ᴛʜᴀɴᴋs 😊]───⍟"""


    HELP_TEXT = """💡 Just Send Me Your Photo And I'll Upload it To You .  That's it

❤ [Donate](https://t.me/Benwolf24) (PayPal)
"""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @Rex_Bots_Support",

    WAIT = "💬 Please Wait !!"
