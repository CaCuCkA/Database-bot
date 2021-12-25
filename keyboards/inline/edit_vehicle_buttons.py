from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import edit_vehicle_callback

edit_vehicle_keyboard = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text="Изменить модель",
                                                         callback_data=edit_vehicle_callback.new(
                                                             function_name="model")
                                                     )
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text="Посадить водителя",
                                                         callback_data=edit_vehicle_callback.new(
                                                             function_name="pull_in")
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="Высадить водителя",
                                                         callback_data=edit_vehicle_callback.new(
                                                             function_name="pull_off")
                                                     )
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text="Изменить номер",
                                                         callback_data=edit_vehicle_callback.new(function_name="plat")
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="Удалить автомобиль",
                                                         callback_data=edit_vehicle_callback.new(function_name="delete")
                                                     )
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text="Отмена",
                                                         callback_data=edit_vehicle_callback.new(function_name="cancel")
                                                     )
                                                 ]
                                             ])
