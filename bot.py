#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.DEBUG,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)

def welcome(bot, update):
	for new_user_obj in update.message.new_chat_members:
		chat_id = update.message.chat.id
		new_user = ""

		try:
			new_user = "@" + new_user_obj['username']

		except Exception as e:
			new_user = new_user_obj['first_name']

		bot.send_message(chat_id=chat_id, text=" %s Welcome to BOScoin! Please read the pinned post. Feel free to ask questions. Thanks." % new_user)

welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
updater.dispatcher.add_handler(welcome_handler)

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
