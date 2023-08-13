#(©)AnimeCodeHub

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNELS, CHANNEL_ID, PORT
#from giphy_client.giphy_client import DefaultApi

#import random

#from config import GIPHY_API_KEY
#giphy = DefaultApi(api_key=GIPHY_API_KEY)

#@Client.on_message(filters.command('hug'))
#async def hug_command_handler(client, message):
    #try:

        #Get a random "hug" GIF from Giphy

        #response = giphy.gifs_search_get(GIPHY_API_KEY, 'hug')
       # gifs = response.data
       # gif = random.choice(gifs)

        # Send the GIF to the user
        #await client.send_animation(chat_id=message.chat.id, animation=gif.images.original.url)
   # except ApiException as e:
            #print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

name ="""

Hmm?
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()



        if FORCE_SUB_CHANNELS:
             self.invitelink = []
        for channel_id in FORCE_SUB_CHANNELS:
        try:
            link = (await self.get_chat(channel_id)).invite_link
        if not link:
                await self.export_chat_invite_link(channel_id)
                link = (await self.get_chat(channel_id)).invite_link
            self.invitelink.append(link)
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
            self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNELS value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {channel_id}")
            self.LOGGER(__name__).info("\nBot Stopped. ")
            sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!")
        self.LOGGER(__name__).info(f""" \n\n  hm?
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
