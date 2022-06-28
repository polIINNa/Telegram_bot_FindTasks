import logging
from aiogram import Bot, Dispatcher, executor, types
import config

import parse
import earnings



#configure logging (P.S. Не совсем пока понимаю что это и зачем, но вроде оно нужно)
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TELEGRAM_API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    mess = f'Хей, <b>{message.from_user.first_name}</b>. Сейчас посмотрим, какие задания могу для тебя найти'
    await message.answer(mess, parse_mode='html')
    for i in parse.find_tasks():
        await message.answer(i)


@dp.message_handler(commands=['addearning'])
async def add_earning_ask(message: types.Message):
    mess = f'Ее, <b>{message.from_user.first_name}</b>, поздарвляю с выполненным заданием!\nСколько удалось заработать?'
    await message.answer(mess, parse_mode='html')


@dp.message_handler(commands=['showearnings'])
async def show_earnings(message: types.Message):
    earnings_sum = 0
    for i in earnings.all_earnings():
        earnings_sum += i.price
    await message.answer(f'Суммарный заработок: {earnings_sum}')


@dp.message_handler(content_types=['text'])
async def add_earning(message: types.Message):
    try:
        new_earning = earnings.add_earning(message.text)
        mess = f'Было добавлено {new_earning.price} рублей'
    except ValueError:
        mess = f'Прости, <b>{message.from_user.first_name}</b>:(  Не могу понять это сообщение'
    await message.answer(mess, parse_mode='html')


if __name__ == '__main__':
    #launch bot
    executor.start_polling(dp, skip_updates=True)
