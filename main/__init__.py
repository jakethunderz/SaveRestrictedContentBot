#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27151403
API_HASH = "6edad223fa83bfd56ee779d3d715546e"
BOT_TOKEN = "5370264821:AAH6hF3eYcFaKm1ZjPnWygiVbTvyt3lRfp4"
SESSION = "BQAPaydkzV7V980xbz5pGikD_c1KR6DN16CkdJ7XC8cZpurY4KuX-YQ-2WARD_ldwkUY3m9ty5uGzWeLa0TelEviHCSbrb-jL73r8bcN757WgOFCb18N9yz6Sf43-vm9y-NR-mcBAd_ANNCCbUs-1f2HVjJoNLTM9wlMjhT4zXvV1GUGzDyfWFFeVqXrOhyrLj9JpyZQQfP2U6DvQp-kbYKFKMgWIYGF_J6kYulixXo9aDz4oRD077GAYIp_b9mJSu0duxFMsWRDL84N4yfMwJ4q44BqO3tmWISXvfok0oA2W2HUzAmBi5iyGxocOh2xa3SzQAnI6MtTT9UPIEaDneFUAAAAATywpXgA"
FORCESUB = "flashxlibrary"
AUTH = 5313176952

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
