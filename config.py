#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6253669210:AAGiUM6kodf9CPuIEXnCpkJ6geJRuwpRQhw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27465363"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ab1f1342001710875db59dfc6a77749f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001534956289"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5799637320"))

#Port
PORT = os.environ.get("PORT", "9001")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://peerzadasuhaib352:Xsk4gVMajYhK4mwf@cluster0.mo4v2lv.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001387951837"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>👋 ʜɪ {first} </b>, <b> ɪᴄʜɪɢᴏ ʜᴇʀᴇ ✦ , </b> \n кєєρ ωαт¢нιиg 🍿 \n кєєρ ѕυρρσятιиg 🙋🏻‍♀️ ")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5687950438 1277025786 597515629 1949894745 5606837601 1068449033 1501687881 6015466432").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋Mucho Gusto {first} ! \n Please Join Main channel \n [ ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ ⚡ ] \n then Download by tapping on \n ⚡ʀᴇʟᴏᴀᴅ  \n Thank You ⚡")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>⚡ My today work hours are </b>\n{uptime} \n Ocean forever 🌊 "
USER_REPLY_TEXT = "<b> <a href='tg://settings/'>click here.. Hi \n Tap on \help or \start for any issue ⚡   </b> "

ADMINS.append(OWNER_ID)
ADMINS.append(5799637320)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
