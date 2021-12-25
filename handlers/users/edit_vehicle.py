from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import edit_vehicle_callback
from keyboards.inline.edit_vehicle_buttons import edit_vehicle_keyboard
from loader import vdb, dp

ID = []


def save_id(id):
    ID.append(id)


@dp.message_handler(Command("edit_vehicle"))
async def edit_driver_first(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    database = vdb.select_all_vehicles()
    await message.answer(f"Привет, {name} \n"
                         f"С помощью этой функции ты можешь изменять данные любой машины "
                         f"в твоей базе данных. \n"
                         f"Сейчас я тебе выведу всех, кто у меня есть: \n"
                         f"{database}")
    await message.answer("Напиши айди того, кого хочешь изменить. Подсказка,"
                         " айди - это первая цифра в каждой скобке")
    await state.set_state("vehicle_id")


@dp.message_handler(state="vehicle_id")
async def edit_driver_second(message: types.Message, state: FSMContext):
    id = int(message.text)
    save_id(id)
    await message.answer("Отлично! \n"
                         "Теперь выбери, что ты хочешь сделать\n"
                         "!ЧТОБ ЗАКОНЧИТЬ НАЖМИ 'Отмена'!",
                         reply_markup=edit_vehicle_keyboard)
    await state.finish()


@dp.callback_query_handler(edit_vehicle_callback.filter(function_name="model"))
async def change_model_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите новую марку \n"
                              f"Пример: Lamborghini")
    await state.set_state("new_model")


@dp.message_handler(state="new_model")
async def change_model_second(message: types.Message, state: FSMContext):
    model = message.text
    id = ID[0]
    vehicle_before = vdb.select_vehicle(id=id)
    vdb.update_model(id=id, model=model)
    vehicle_after = vdb.select_vehicle(id=id)
    await message.answer(f"Модель автомобиля с id={id} изменено с {vehicle_before[2]} на {vehicle_after[2]}")
    await state.finish()


@dp.callback_query_handler(edit_vehicle_callback.filter(function_name="plat"))
async def change_plat_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите новый номер \n"
                              f"Пример: АА 0000 СВ")
    await state.set_state("new_plat")


@dp.message_handler(state="new_plat")
async def change_plat_second(message: types.Message, state: FSMContext):
    plat = message.text
    id = ID[0]
    vehicle_before = vdb.select_vehicle(id=id)
    vdb.update_plate_number(id=id, plate_number=plat)
    vehicle_after = vdb.select_vehicle(id=id)
    await message.answer(f"Номер автомобиля с id={id} изменено с {vehicle_before[3]} на {vehicle_after[3]}")
    await state.finish()


@dp.callback_query_handler(edit_vehicle_callback.filter(function_name="pull_in"))
async def pull_in_first(call: CallbackQuery, state: FSMContext):
    id = ID[0]
    vehicle = vdb.select_vehicle(id=id)
    driver = vehicle[1]
    await call.answer(cache_time=60)
    if driver is None:
        await call.message.answer("Введите id водителя, которого хотите посадить")
        await state.set_state("set_driver")
    else:
        await call.answer("Водитель уже имеется!", show_alert=True)


@dp.message_handler(state="set_driver")
async def pull_in_second(message: types.Message, state: FSMContext):
    driver_id = int(message.text)
    id = ID[0]
    vdb.update_driver_id(id=id, driver_id=driver_id)
    await message.answer(f"Теперь в машине с id={id} сидит водитель с id={driver_id}")
    state.finish()


@dp.callback_query_handler(edit_vehicle_callback.filter(function_name="pull_off"))
async def pull_off(call: CallbackQuery):
    id = ID[0]
    vehicle = vdb.select_vehicle(id=id)
    driver = vehicle[1]
    await call.answer(cache_time=60)
    if driver is not None:
        up_driver = vdb.update_driver_id(driver_id=None, id=id)
        await call.message.answer(f"Мы изменили статус, теперь у вашей машины не водителя {up_driver[1]}")
    else:
        await call.answer("Водитель отсутсвует!", show_alert=True)


@dp.callback_query_handler(edit_vehicle_callback.filter(function_name="delete"))
async def delete(call: CallbackQuery):
    id = ID[0]
    vdb.delete_vehicle(id=id)
    await call.answer("Машина удалена!", show_alert=True)


@dp.callback_query_handler(edit_vehicle_callback.filter(function_name="cancel"))
async def cancel(call: CallbackQuery):
    await call.answer("Вы вышли", show_alert=True)
    await call.message.edit_reply_markup()
    ID.pop(0)
