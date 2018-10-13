# -*- coding: utf-8 -*-

from telegram.ext import Updater
updater = Updater(token='672249649:AAFVgl1vI5cZ83qp_Zm1gkFmCYAMiKZw7mQ')

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
                     
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


updater.start_polling()
