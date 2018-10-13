# -*- coding: utf-8 -*-
import os
TOKEN = os.environ["TOKEN"]
from telegram.ext import Updater
updater = Updater(TOKEN)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
                     
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


updater.start_polling()
