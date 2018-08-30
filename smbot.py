# -*- coding: utf-8 -*-
import telepot
import time
import random
from telepot.loop import MessageLoop

# this variable must be changed by the bot registration key
bot_key = "botky"

# instance of sm-bot
bot = telepot.Bot(bot_key)

# this method handles the messages and prepares the sm-bot' response
def handle(msg):
	# get the chat id
	chat_id = msg["chat"]["id"]
	
	# get the messages and turn them into lowercase
	msj = msg["text"]
	msj = msj.lower()
	
	# prepare response depending on the available words within the message
	if "maquina" in msj:
		bot.sendMessage(chat_id, "Fascista!")


MessageLoop(bot, handle).run_as_thread()

while 1:
time.sleep(10)
