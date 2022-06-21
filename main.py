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
    mess = f'Хей, <b>{message.from_user.first_name}</b>. Есть желание подзаработать?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but1, but2 = types.KeyboardButton('Погнали'), types.KeyboardButton('Нет')
    markup.add(but1, but2)
    await message.answer(mess, parse_mode='html', reply_markup=markup)


@dp.message_handler(commands=['addearning'])
async def add_earning_ask(message: types.Message):
    mess = f'Ее, {message.from_user.first_name}, поздарвляю с выполненным заданием!\nСколько удалось заработать?'
    await message.answer(mess)


@dp.message_handler(commands=['showearnings'])
async def show_earnings(message: types.Message):
    for earn in earnings.show_earnings():
        await message.answer(earn.price)


@dp.message_handler()
async def add_earning(message: types.Message):
    new_earning = earnings.add_earning(message.text)
    await message.answer(f'Было добавлено {new_earning.price} рублей')


@dp.message_handler(content_types=['text'])
async def get_user_text(message: types.Message):
    if message.text == 'Нет':
        await message.answer("<u>Ну... ладно</u>", parse_mode='html')
    elif message.text == 'Погнали':
        for i in parse.find_tasks():
            await message.answer(i)


if __name__ == '__main__':
    #launch bot
    executor.start_polling(dp, skip_updates=True)
