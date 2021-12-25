from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, dbd


def parsing_str(string: str):
    return list(map(str, string.split(" ")))


@dp.message_handler(Command("add_driver"))
async def add_driver_first_step(message: types.Message, state: FSMContext):
    await message.answer("Для регистрации нового пользователя"
                         "мне нужны некоторые данные от тебя: \n"
                         "1.id - индифакационный номер водителя (натуральное число).\n"
                         "2.First name - персональное имя водителя (строка).\n"
                         "3.Last name - фамилия водителя (строка). \n"
                         "P.S Пожалуйста, следуй инструкциям. \n"
                         "Пример правильной записи: 1 Иван Иванович")
    drivers = dbd.select_all_drivers()
    await message.answer(f"Сейчас я тебе отправлю список водителей до регистрации: \n"
                         f"{drivers}")
    await state.set_state("new_driver")


@dp.message_handler(state="new_driver")
async def add_driver_second_step(message: types.Message, state: FSMContext):
    string = message.text
    parsing_list = parsing_str(string)
    dbd.add_driver(Id=int(parsing_list[0]), first_name=parsing_list[1], last_name=parsing_list[-1])
    driver = dbd.select_driver(id=int(parsing_list[0]))
    drivers = dbd.select_all_drivers()
    await message.answer(f"Водитель успешно зарегестрирован: \n"
                         f" {driver}")
    await message.answer(f"База данных после регестрации водителя: \n"
                         f"{drivers}")
    await state.finish()

