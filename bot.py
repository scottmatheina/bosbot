#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.DEBUG,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)

def delete(bot, update):
	message = update.message.text.lower()
	ban = ['retard',
		'retarded',
		'slut',
		'dyke',
		'retards',
		'nigger',
		'bitch',
		'whore',
		'queer',
		'fuck',
		'fag',
		'cunt',
		]
	for i in ban:
		if i in message:
			update.message.delete()

delete_handler = MessageHandler(Filters.text, delete)
updater.dispatcher.add_handler(delete_handler)

updater.start_polling()
updater.idle()
