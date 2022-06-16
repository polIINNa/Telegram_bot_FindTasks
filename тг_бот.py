import telebot
from bs4 import BeautifulSoup
import requests


bot = telebot.TeleBot('5591112751:AAG5kRQfwTFtyJujFHROEa0oXZEkZ2B0XK8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>. Есть желание подзаработать?'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    url = "https://freelance.habr.com/tasks"
    my_tasks = []
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    for task in soup.findAll('article', class_="task task_list"):
        for item in task.findAll('a', class_="tags__item_link"):
            if item.string.lower() == 'python' or item.string.lower() == "пайтон" or item.string.lower() == "питон":
                if task not in my_tasks:
                    my_tasks.append(task)
                    task_name = task.find('div', 'task__title').string
                    task_href = task.find('a').get('href')
                    bot.send_message(message.chat.id, task_name)
                    bot.send_message(message.chat.id, f'https://freelance.habr.com/{task_href}')


bot.polling(none_stop=True)
