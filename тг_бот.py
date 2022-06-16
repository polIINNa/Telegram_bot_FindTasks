import telebot

bot = telebot.TeleBot('5591112751:AAG5kRQfwTFtyJujFHROEa0oXZEkZ2B0XK8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)
