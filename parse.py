'''Поиск заданий, парсинг сайта'''
from bs4 import BeautifulSoup
import requests


def find_tasks():
    url = "https://freelance.habr.com/tasks"
    my_tasks = []
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    for task in soup.findAll('article', class_="task task_list"):
        for item in task.findAll('a', class_="tags__item_link"):
            if item.string.lower() == 'python' or item.string.lower() == "пайтон" or item.string.lower() == "питон":
                if task not in my_tasks:
                    my_tasks.append(task)
    if my_tasks == []:
        yield ('Пока нет подходящих заданий, сидим без деняк')
    else:
        for task in my_tasks:
            task_name = task.find('div', 'task__title').string
            task_href = task.find('a').get('href')
            yield (f"Название таска: {task_name}\nСслыка на таск: https://freelance.habr.com{task_href}")


