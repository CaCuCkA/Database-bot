from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import vehicle_callback

vehicle_func = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Список автомобилей",
                                                callback_data=vehicle_callback.new(function_name="vehicle_list")
                                            )
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="С водителем",
                                                callback_data=vehicle_callback.new(function_name="with_driver")
                                            ),
                                            InlineKeyboardButton(
                                                text="БЕЗ водителя",
                                                callback_data=vehicle_callback.new(function_name="without_driver")
                                            )
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Удалить все",
                                                callback_data=vehicle_callback.new(function_name="delete_all")
                                            )
                                        ],
[
                                            InlineKeyboardButton(
                                                text="Отмена",
                                                callback_data=vehicle_callback.new(function_name="cancel")
                                            )
                                        ]
                                    ])
