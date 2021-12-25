from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import edit_driver_callback
from keyboards.inline.edit_driver_buttons import edit_driver_keyboard
from loader import dp, dbd

ID = []


def save_id(id):
    ID.append(id)


@dp.message_handler(Command("edit_driver"))
async def edit_driver_first(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    database = dbd.select_all_drivers()
    await message.answer(f"Привет, {name} \n"
                         f"С помощью этой функции ты можешь изменять данные любого водителя "
                         f"в твоей базе данных. \n"
                         f"Сейчас я тебе выведу всех, кто у меня есть: \n"
                         f"{database}")
    await message.answer("Напиши айди того, кого хочешь изменить. Подсказка,"
                         " айди - это первая цифра в каждой скобке")
    await state.set_state("driver_id")


@dp.message_handler(state="driver_id")
async def edit_driver_second(message: types.Message, state: FSMContext):
    id = int(message.text)
    save_id(id)
    await message.answer("Отлично! \n"
                         "Теперь выбери, что ты хочешь сделать\n"
                         "!ЧТОБ ЗАКОНЧИТЬ НАЖМИ 'Отмена'!",
                         reply_markup=edit_driver_keyboard)
    await state.finish()


@dp.callback_query_handler(edit_driver_callback.filter(function_name="joining_date"))
async def change_date_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите, новую дату \n"
                              f"Пример: 12-11-2010")
    await state.set_state("new_date")


@dp.message_handler(state="new_date")
async def change_date_second(message: types.Message, state: FSMContext):
    date = message.text
    id = ID[0]
    driver_before = dbd.select_driver(id=id)
    dbd._DriverDataBase__update_joining_date(joiningDate=date, Id=id)
    driver_after = dbd.select_driver(id=id)
    await message.answer(f"Время регистрации водителя с id={id} изменено с {driver_before[3]} на {driver_after[3]}")
    await state.finish()


@dp.callback_query_handler(edit_driver_callback.filter(function_name="update_f_name"))
async def change_f_name_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите, новое имя \n"
                              f"Пример: Иван")
    await state.set_state("new_f")


@dp.message_handler(state="new_f")
async def change_f_name_second(message: types.Message, state: FSMContext):
    f_name = message.text
    id = ID[0]
    driver_before = dbd.select_driver(id=id)
    dbd.update_first_name(first_name=f_name, Id=id)
    driver_after = dbd.select_driver(id=id)
    await message.answer(f"Имя водителя с id={id} изменено с {driver_before[1]} на {driver_after[1]}")
    await state.finish()


@dp.callback_query_handler(edit_driver_callback.filter(function_name="update_l_name"))
async def change_l_name_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите, новую фамилию\n"
                              f"Пример: Иванов")
    await state.set_state("new_l")


@dp.message_handler(state="new_l")
async def change_l_name_second(message: types.Message, state: FSMContext):
    l_name = message.text
    id = ID[0]
    driver_before = dbd.select_driver(id=id)
    dbd.update_last_name(last_name=l_name, Id=id)
    driver_after = dbd.select_driver(id=id)
    await message.answer(f"Фамилия водителя с id={id} изменено с {driver_before[2]} на {driver_after[2]}")
    await state.finish()


@dp.callback_query_handler(edit_driver_callback.filter(function_name="delete"))
async def delete(call: CallbackQuery):
    id = ID[0]
    dbd.delete_driver(id=id)
    await call.answer("Пользователь удален!", show_alert=True)


@dp.callback_query_handler(edit_driver_callback.filter(function_name="cancel"))
async def cancel(call: CallbackQuery):
    await call.answer("Вы вышли", show_alert=True)
    await call.message.edit_reply_markup()
    ID.pop(0)