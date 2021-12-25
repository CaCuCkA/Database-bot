import emoji
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import edit_driver_callback

edit_driver_keyboard = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=emoji.emojize(":red_exclamation_mark:"
                                                                           "Изменить дату "
                                                                           "регистрации:red_exclamation_mark:"),
                                                        callback_data=edit_driver_callback.new(
                                                            function_name="joining_date")
                                                    )
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text="Изменить имя",
                                                        callback_data=edit_driver_callback.new(
                                                            function_name="update_f_name")
                                                    ),
                                                    InlineKeyboardButton(
                                                        text="Изменить фамилию",
                                                        callback_data=edit_driver_callback.new(
                                                            function_name="update_l_name")
                                                    ),
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text="Удалить пользователя",
                                                        callback_data=edit_driver_callback.new(
                                                            function_name="delete")
                                                    )
                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text="Отмена",
                                                        callback_data=edit_driver_callback.new(
                                                            function_name="cancel")
                                                    )
                                                ]
                                            ])
