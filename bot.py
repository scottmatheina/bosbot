#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from msg_list import message_list
token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.DEBUG,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)

#def announcments(bot, job):
#	chat_id = update.message.chat.id
#	message_list = random.choice([
#			'text1',
#			'text2',
#			'text3'
#			])
#
#	bot.send_message(chat_id=chat_id, text='textkksks')

#updater.job_queue.run_repeating(announcments, interval=5, first=0)

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

def welcome(bot, update):

	for new_user_obj in update.message.new_chat_members:
		chat_id = update.message.chat.id

		new_user = ""

		try:
			new_user = "@" + new_user_obj['username']

		except Exception as e:
			new_user = new_user_obj['first_name']

		message = random.choice(message_list)
		bot.send_message(chat_id=chat_id, text="{0} Welcome! {1}".format(new_user, message))

welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
updater.dispatcher.add_handler(welcome_handler)

updater.start_polling()
updater.idle()
