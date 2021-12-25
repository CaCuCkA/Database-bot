from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, vdb


def parsing_str(string: str):
    return list(map(str, string.split(" ")))


@dp.message_handler(Command("add_vehicle"))
async def add_vehicle(message: types.Message, state: FSMContext):
    await message.answer("Для регистрации нового автомобиля"
                         "мне нужны некоторые данные от тебя: \n"
                         "1.id - индифакационный номер автомобиля (натуральное число).\n"
                         "2.model - модель автомобиля (строка).\n"
                         "3.plat number - номер автомоюиля (строка). \n"
                         "P.S Пожалуйста, следуй инструкциям. \n"
                         "Пример правильной записи: 1 Volvo AA-0000-CB")
    vehicle = vdb.select_all_vehicles()
    await message.answer(f"Сейчас я тебе отправлю список автомобилей до регистрации: \n"
                         f"{vehicle}")
    await state.set_state("new_vehicle")

    @dp.message_handler(state="new_vehicle")
    async def add_driver_second_step(message: types.Message, state: FSMContext):
        string = message.text
        parsing_list = parsing_str(string)
        id = int(parsing_list[0])
        model = parsing_list[1]
        plate_number = parsing_list[-1].replace("-", " ")
        vdb.add_vehicle(id=id, model=model, plate_number=plate_number)
        vehicle = vdb.select_vehicle(id=id)
        vehicles = vdb.select_all_vehicles()
        await message.answer(f"Автомобиль успешно зарегестрирован: \n"
                             f" {vehicle}")
        await message.answer(f"База данных после регестрации автомобиля: \n"
                             f"{vehicles}")
        await state.finish()
