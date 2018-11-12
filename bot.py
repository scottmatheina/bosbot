#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import MessageEntity
from msg_list import message_list
token = os.environ.get("TOKEN")
logging.basicConfig(level=logging.INFO,
		    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token)

def delete_post(bot, update):
	update.message.delete()
	chat_id = update.message.chat.id
	bot.send_message(chat_id=chat_id, text='Deleted, allowed document types are\
	stickers, photos, and gifs')

delete_post_handler = MessageHandler((Filters.document |
					  Filters.audio |
					  Filters.voice |
					  Filters.video_note |
					  Filters.video |
					  Filters.location |
					  Filters.contact) & (~ Filters.document.gif),
					  delete_post)

updater.dispatcher.add_handler(delete_post_handler)

def remove_text(bot, update):
	message = update.message.text.lower()
	words = ['bostoken',
		 'bos token'
		]
	for i in words:
		if i in message:
			update.message.delete()
			chat_id = update.message.chat.id
			bot.send_message(chat_id=chat_id, text='Deleted, BOSTOKEN\
 is a completely different project, not associated\
 with us at all')

remove_text_handler = MessageHandler(Filters.text, remove_text)

updater.dispatcher.add_handler(remove_text_handler)

def remove_text_link(bot, update):
	message = update.message.text.lower()
	words = ['pump',
		'signal',
		'profit',
		'signals'
		]
	for i in words:
		if i in message:
			update.message.delete()
			chat_id = update.message.chat.id
			bot.send_message(chat_id=chat_id, text='Deleted, Spam')

remove_text_link_handler = MessageHandler(
	Filters.text & (Filters.entity(MessageEntity.URL) |
                        Filters.entity(MessageEntity.TEXT_LINK)),
	remove_text_link)

updater.dispatcher.add_handler(remove_text_link_handler)

def delete_command(bot, update):
	update.message.delete()

delete_command_handler = MessageHandler([Filters.command], delete_command)
updater.dispatcher.add_handler(delete_command_handler)

def delete_bad_language(bot, update):
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
			chat_id = update.message.chat.id
			bot.send_message(chat_id=chat_id, text='Deleted, Inappropriate Language')
			update.message.delete()

delete_bad_language_handler = MessageHandler(Filters.text, delete_bad_language)
updater.dispatcher.add_handler(delete_bad_language_handler)

def welcome(bot, update):

	for new_user_obj in update.message.new_chat_members:
		chat_id = update.message.chat.id

		new_user = ""

		try:
			new_user = "@" + new_user_obj['username']

		except Exception as e:
			new_user = new_user_obj['first_name']

		message = random.choice(message_list)
		bot.send_message(chat_id=chat_id, text="{0} Welcome!\n{1}".format(new_user, message))

welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
updater.dispatcher.add_handler(welcome_handler)

updater.start_polling()
updater.idle()
