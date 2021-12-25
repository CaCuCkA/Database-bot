import emoji
import emoji as emoji
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot

photo = "https://thumbs.dreamstime.com/b/%D0%BC%D0%B8%D0%BB%D1%8B%D0%B9-%D0%B3%D1%80%D1%83%D1%81%D1%82%" \
        "D0%BD%D1%8B%D0%B9-%D0%B7%D0%BB%D0%BE%D0%B9-%D1%80%D0%BE%D0%B1%D0%BE%D1%82-%D0%B1%D0%BE%D1%82-%D0%" \
        "B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80-%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F-%D1%81%D0%BE%D" \
        "0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BF%D0%BB%D0%BE%D1%81%D0%BA%D0%B0%D1%8F-157204441.jpg"


@dp.message_handler(Command("archy"))
async def archy_info(message: types.Message):
    name = message.from_user.full_name
    await bot.send_photo(chat_id=message.from_user.id, photo=photo,
                         caption=emoji.emojize(f"Привет, {name}! \n"
                                               f"Мне очень приятно, что ты мной заинтересовался)\n"
                                               f"Меня зовут Арчи, я твой бот-помощник.\n"
                                               f"Я очень молод, поэтому мой функционал достаточно узкий.\n"
                                               f"Я работаю с базами данных людей и машин. С моей помощью "
                                               f"ты можешь, добавлять, изменять, расширять эти базы + "
                                               f"изменять какие-то данные пользователя.\n"
                                               f"Спасибо, что дал мне шанс помочь тебе :red_heart:"))
