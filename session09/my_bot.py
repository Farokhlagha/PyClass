# pip install pyTelegramBotApi
import random
import telebot
from telebot import types

my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
key1 = types.KeyboardButton("برگشت")
key2 = types.KeyboardButton("فال")
key3 = types.KeyboardButton("ماشین حساب")
key4 = types.KeyboardButton("راهنما")
key5 = types.KeyboardButton("چت بات")
key6 = types.KeyboardButton("دانلود")

my_keyboard.add(key1, key2, key3, key4, key5, key6)





bot = telebot.TeleBot("6658932458:AAH_CEgRQ8LEjInW92R7vyI0Rj8ZlKUgs7Y", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to python bot!\n Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "How can I help you?")

@bot.message_handler(commands=['fal'])
def send_fal(message):
	fal_list = ["به سفر خواهی زفت", "دیدار یار", "فنا"]
	select_fal = random.choice(fal_list)
	bot.send_message(message.chat.id, select_fal)

	

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	#bot.reply_to(message, "This is a simple message.")	
	#bot.send_message(message.chat.id, "This is a simple message.")
	if message.text == "سلام":
		bot.send_message(message.chat.id, "علیک سلام")
	elif message.text == "خوبی؟":
		bot.send_message(message.chat.id, "ممنون")
	elif message.text == "عکس قدی بده":
		photo = open("session9/khoshgel.jpg, rb")
		bot.send_photo(message.chat.id, photo)
	else:
		bot.send_message(message.chat.id, "نمی فهمم چی میگی", reply_markup=my_keyboard)

	
bot.infinity_polling()

