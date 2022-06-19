import logging
from aiogram import Bot, Dispatcher, executor, types
import parse
import config


#configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TELEGRAM_API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    mess = f'Хей, <b>{message.from_user.first_name}</b>. Есть желание подзаработать?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but1 = types.KeyboardButton('Погнали')
    but2 = types.KeyboardButton('Нет')
    markup.add(but1, but2)
    await message.answer(mess, parse_mode='html', reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def get_user_text(message):
    if message.text == 'Нет':
        await message.answer("<u>Ну... ладно</u>", parse_mode='html')
    elif message.text == 'Да':
        for i in parse.find_tasks():
            await message.answer(i)


if __name__ == '__main__':
    #launch bot
    executor.start_polling(dp, skip_updates=True)
