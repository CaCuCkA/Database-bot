from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \n"
                         f"Я твой бот-помощник. Меня зовут Арчи. \n"
                         f"Давай я тебя в введу в курс дела: \n"
                         f"Нажми на значок '/', он находиться возле стикеров."
                         f"С помощью его ты можешь узнать, какие команды тебе доступны и что они делают")
