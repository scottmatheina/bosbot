#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.DEBUG,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)

def hello(bot, update):
	update.message.reply_text(
		'Hello {}'.format(update.message.from_user.first_name))
hello_handler = CommandHandler('hello', hello)
updater.dispatcher.add_handler(hello_handler)

def delete(bot, update):
	update.message.delete()
delete_handler = MessageHandler(Filters.text, delete)
updater.dispatcher.add_handler(delete_handler)


updater.start_polling()
updater.idle()
