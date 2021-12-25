from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=emoji.emojize("Driver DataBase :construction_worker:")),
        KeyboardButton(text=emoji.emojize("Vehicle DataBase :delivery_truck:"))
    ],
    [
        KeyboardButton(text="Cancel")
    ]
],
    resize_keyboard=True)
