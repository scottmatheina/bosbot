#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import MessageEntity
from msg_list_en import message_list_en
from msg_list_ru import message_list_ru
token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.DEBUG,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)
ru_chat = -1001341820902
#test account
#ru_chat = -1001434122024

def delete_post(bot, update):
	chat_id = update.message.chat.id
	if chat_id != ru_chat:
		update.message.delete()
		bot.send_message(chat_id=chat_id, text='Deleted, allowed document types are\
		stickers, photos, and gifs, please post using the Photo icon not the File icon.')

delete_post_handler = MessageHandler((Filters.document |
					  Filters.audio |
					  Filters.voice |
					  Filters.video_note |
					  Filters.video |
					  Filters.location |
					  Filters.contact) & (~ Filters.document.gif),
					  delete_post)
updater.dispatcher.add_handler(delete_post_handler)

def delete_post(bot, update):
	chat_id = update.message.chat.id
	message = update.message.text.lower()

	word1 = ['bostoken',
		'bos token'
		]

	word2 = ['retard',
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
	    	'cunt'
	    	]
	for a in word1:
		if a in message:
			if chat_id != ru_chat:
				update.message.delete()
				bot.send_message(chat_id=chat_id, text='Deleted, BOSTOKEN\
 is a completely different project, not associated\
 with us at all')

	for b in word2:
		if b in message:
			if chat_id != ru_chat:
				bot.send_message(chat_id=chat_id, text='Deleted, Inappropriate Language')
				update.message.delete()

delete_post_handler = MessageHandler(Filters.text, delete_post)
updater.dispatcher.add_handler(delete_post_handler)

def delete_command(bot, update):
	chat_id = update.message.chat.id
	if chat_id != ru_chat:
		update.message.delete()

delete_command_handler = MessageHandler([Filters.command], delete_command)
updater.dispatcher.add_handler(delete_command_handler)

def welcome(bot, update):

	for new_user_obj in update.message.new_chat_members:
		chat_id = update.message.chat.id

		new_user = ""

		try:
			new_user = "@" + new_user_obj['username']

		except Exception as e:
			new_user = new_user_obj['first_name']

		message_en = random.choice(message_list_en)
		message_ru = random.choice(message_list_ru)
		## BOSmodDev ru testing
		if chat_id == ru_chat:
			bot.send_message(chat_id=ru_chat, text="{0} Приветствуем!\n{1}".format(new_user, message_ru))
		else:
			bot.send_message(chat_id=chat_id, text="{0} Welcome!\n{1}".format(new_user, message_en))

welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
updater.dispatcher.add_handler(welcome_handler)

updater.start_polling()
updater.idle()