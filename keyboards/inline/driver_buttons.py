from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import driver_callback

driver_func = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="Список водителей",
                                               callback_data=driver_callback.new(function_name="driver_list")
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text="Созданы ДО",
                                               callback_data=driver_callback.new(function_name="created_before")
                                           ),
                                           InlineKeyboardButton(
                                               text="Созданы ПОСЛЕ",
                                               callback_data=driver_callback.new(function_name="created_after")
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text="Удалить всех",
                                               callback_data=driver_callback.new(function_name="delete_all")
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text="Отмена",
                                               callback_data=driver_callback.new(function_name="cancel")
                                           )
                                       ]
                                   ])
