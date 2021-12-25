from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - P.S меня ты уже нажимал. Если хочешь поздороватся та кликни, мне не сложно)",
            "/help - Нажми на меня и я помогу тебе с командами",
            "/archy - Кто я такой?",
            "/menu - набор функций для работы с БД",
            "/add_driver - добавить водителя",
            "/add_vehicle - добавить автомобиль",
            "/edit_driver - изменить данные водителя",
            "/edit_vehicle - изменить данные автомобиля")
    
    await message.answer("\n".join(text))
