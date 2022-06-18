import telebot
import parse
from telebot import types

bot = telebot.TeleBot('5591112751:AAG5kRQfwTFtyJujFHROEa0oXZEkZ2B0XK8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Хей, <b>{message.from_user.first_name}</b>. Есть желание подзаработать?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but1 = types.KeyboardButton('Да')
    but2 = types.KeyboardButton('Погнали')
    markup.add(but1, but2)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "И тебе привет, ленивая жопка!", parse_mode='html')
    elif message.text == 'Да' or message.text == 'Погнали':
        for i in parse.find_tasks():
            bot.send_message(message.chat.id, i)


bot.polling(none_stop=True)
