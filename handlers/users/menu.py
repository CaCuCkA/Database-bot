import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.default import menu
from keyboards.inline.callback_datas import driver_callback, vehicle_callback
from keyboards.inline.driver_buttons import driver_func
from keyboards.inline.vehicle_buttons import vehicle_func
from loader import dp, bot, dbd, vdb

photo_id = {
    "DriverDataBase": "https://icon-library.com/images/database-management-icon/database-management-icon-16.jpg",
    "VehicleDataBase": "https://e7.pngegg.com/pngimages/274/498/png-clipart-database-information-system-big-data-base"
                       "-miscellaneous-angle-thumbnail.png "
}


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Вы вызвали список доступных функций.", reply_markup=menu)


@dp.message_handler(text=emoji.emojize("Driver DataBase :construction_worker:"))
async def driver_data_base(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id['DriverDataBase'],
                         caption="Доступмные вам функции: ", reply_markup=driver_func)


@dp.message_handler(text=emoji.emojize("Vehicle DataBase :delivery_truck:"))
async def vehicle_data_base(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id['VehicleDataBase'],
                         caption="Доступмные вам функции: ", reply_markup=vehicle_func)


@dp.callback_query_handler(driver_callback.filter(function_name="driver_list"))
async def show_data(call: CallbackQuery):
    drivers = dbd.select_all_drivers()
    await call.answer(cache_time=60)
    await call.message.answer(f"Список водителей зарегистрированных на данный момент: \n"
                              f"{drivers}")


@dp.callback_query_handler(driver_callback.filter(function_name="created_before"))
async def created_before_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите, пожалуйста, дату как показано в примере: \n"
                              f"Пример: 18-12-21")
    await state.set_state("b_date")


@dp.message_handler(state="b_date")
async def created_before_second(message: types.Message, state: FSMContext):
    date = message.text
    drivers = dbd.drivers_filter_created_before(date)
    await message.answer(f"Водители зарегистрированые до {date}\n"
                         f"{drivers}")
    await state.finish()


@dp.callback_query_handler(driver_callback.filter(function_name="created_after"))
async def created_after_first(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer(f"Введите, пожалуйста, дату как показано в примере: \n"
                              f"Пример: 18-12-21")
    await state.set_state("a_date")


@dp.message_handler(state="a_date")
async def created_after_second(message: types.Message, state: FSMContext):
    date = message.text
    drivers = dbd.drivers_filter_created_after(date)
    await message.answer(f"Водители зарегистрированые после {date}\n"
                         f"{drivers}")
    await state.finish()


@dp.callback_query_handler(driver_callback.filter(function_name="delete_all"))
async def delete_all(call: CallbackQuery):
    await call.answer(cache_time=60)
    try:
        dbd.delete_all()
        await call.answer(f"Вы очистили базу данных", show_alert=True)
    except Exception as error:
        print(error)
        await call.answer("База данных - пуста", show_alert=True)


@dp.callback_query_handler(driver_callback.filter(function_name="cancel"))
async def cancel(call: CallbackQuery):
    await call.answer("Вы вышли", show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(vehicle_callback.filter(function_name="vehicle_list"))
async def vehicle_list(call: CallbackQuery):
    vehicle = vdb.select_all_vehicles()
    await call.answer(cache_time=60)
    await call.message.answer(f"Список автомобилей зарегистрированных на данный момент: \n"
                              f"{vehicle}")


@dp.callback_query_handler(vehicle_callback.filter(function_name="with_driver"))
async def vehicle_with_driver(call: CallbackQuery):
    vehicles = vdb.vehicle_with_driver()
    await call.answer(cache_time=60)
    await call.message.answer(f"Список автомобилей c водителем: \n"
                              f"{vehicles}")


@dp.callback_query_handler(vehicle_callback.filter(function_name="without_driver"))
async def vehicle_without_driver(call: CallbackQuery):
    vehicles = vdb.vehicle_without_driver()
    await call.answer(cache_time=60)
    await call.message.answer(f"Список автомобилей без водителя: \n"
                              f"{vehicles}")


@dp.callback_query_handler(vehicle_callback.filter(function_name="delete_all"))
async def delete_all(call: CallbackQuery):
    await call.answer(cache_time=60)
    try:
        vdb.delete_all()
        await call.answer(f"Вы очистили базу данных", show_alert=True)
    except Exception as error:
        print(error)
        await call.answer("База данных - пуста", show_alert=True)


@dp.callback_query_handler(vehicle_callback.filter(function_name="cancel"))
async def cancel(call: CallbackQuery):
    await call.answer("Вы вышли", show_alert=True)
    await call.message.edit_reply_markup()
