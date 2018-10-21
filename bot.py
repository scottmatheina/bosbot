#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.DEBUG,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)
def delete_command(bot, update):
	update.message.delete()

delete_command_handler = MessageHandler([Filters.command], delete_command)
updater.dispatcher.add_handler(delete_command_handler)

def delete_ban(bot, update):
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

delete_ban_handler = MessageHandler(Filters.text, delete_ban)
updater.dispatcher.add_handler(delete_ban_handler)

updater.start_polling()
updater.idle()
