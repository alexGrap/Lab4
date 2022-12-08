from telebot import TeleBot
from telebot import types
import requests
from PIL import Image
from urllib.request import urlopen
import random

bot = TeleBot('5948782307:AAHSiAZLhZ-8JC5xjuwIp26PfSOT5nBmqkQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'This bot can suggest you random activity or send you random cat\'s photo')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Cat)")
    btn2 = types.KeyboardButton("Activity")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Make you choose", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Cat)":
        bot.send_photo(message.chat.id, get_catty(random.randint(1, 2)))
    elif message.text == "Activity":
        bot.send_message(message.from_user.id, get_activity())
    else:
        error(message)


@bot.message_handler(content_types=['voice'])
def error(message):
    bot.send_message(message.from_user.id, "Upsy, doesn't work...)")


@bot.message_handler(content_types=['photo'])
def error(message):
    bot.send_message(message.from_user.id, "Upsy, doesn't work...)")


def get_catty(key):
    arr_rand = [100, 101, 102, 103, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401,
                402, 403, 404, 405, 406, 409, 418, 423, 429, 499, 500, 501, 502, 504, 506, 521, 522, 599]
    rand = random.choice(arr_rand)
    if key == 1:
        url = "https://http.cat/" + rand.__str__()
    else:
        url = "https://cataas.com/cat"
    image = Image.open(urlopen(url))
    return image


def get_activity():
    url = "http://www.boredapi.com/api/activity/"
    data = requests.get(url).json()
    final = data['activity'] + '\n'
    if (data['participants'] > 1):
        final += "You need " + str(data['participants'] - 1) + " friends"
    else:
        final += "You doesn't need anyone for that) Enjoy!"
    return final


bot.polling(none_stop=True, interval=0)
