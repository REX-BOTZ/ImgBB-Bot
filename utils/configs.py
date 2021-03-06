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
๐ Hi ! {} Welcome To @ImgBBRexBot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """
โญโโโโ[โก แดสแดแดแด โก]โโโโ
โ
โ<b>๐ค ๐ฑ๐๐ ๐ฝ๐๐๐ : <a href='https://t.me/IMGBBRexBot'>ษชแดษขสส</a></b>
โ
โ<b>๐ข ๐ฒ๐๐๐๐๐๐  : <a href='https://t.me/Rex_Botz'>แดแดษชษด</a></b>
โ
โ<b>๐ฅ ๐๐๐๐๐๐๐  : <a href='https://t.me/Rex_Bots_Support'>0.9.2สแดแดแด</a></b>
โ
โ<b>๐ข ๐๐๐๐๐๐   : <a href='https://github.com/REX-BOTZ/'>แดแดแดสแดส</a></b>
โ
โ<b>๐ ๐๐๐๐๐๐   : <a href='https://heroku.com'>สแดสแดแดแด</a></b>
โ
โ<b>๐ ๐ป๐๐๐๐๐๐ข  : <a href='https://github.com/pyrogram'>แดสษข1.2.8</a></b>
โ
โ<b>ใ ๐ป๐๐๐๐๐๐๐ : <a href='https://www.python.org'>แดส3.9.4</a></b>
โ
โ<b>๐จโ๐ป ๐ณ๐๐      : <a href='https://t.me/BENWOLF24'>แดกแดสา24</a></b>
โ
โ<b>๐ธ ๐ฟ๐๐ ๐๐๐๐  : <a href='https://t.me/FluxPlay'>าสแดxแดสแดส</a></b>
โ
โฐโโโโโโ[แดสแดษดแดs ๐]โโโโ"""


    HELP_TEXT = """๐ก Just Send Me Your Photo And I'll Upload it To You .  That's it

โค [Donate](https://t.me/Benwolf24) (PayPal)
"""

    ERR_TEXT = "โ ๏ธ API Not Found"

    ERRTOKEN_TEXT = "๐ถ The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @Rex_Bots_Support",

    WAIT = "๐ฌ Please Wait !!"
