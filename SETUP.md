# YALANTIS HOMEWORK

## Archy Telegram bot Setup

![](https://st.depositphotos.com/1052079/2494/v/600/depositphotos_24943249-stock-illustration-gears-on-a-white-background.jpg)
___

## How to find the database?
### If you want to find files that contain all the functions for working with databases. You will need to go down this path "Yalantis_homework\utils\dp_api".
<img src="screenshots\data_path.jpg" width="300">

### There are five files in this file.
 + __inti__ - makes a package out of the file. (! IS NOT RECOMMENDED TO BE TOUCHED)
+ <b>drivers_base</b> - stores all the class, which in its turn has all the necessary functions to work with the driver's database
+ <b>vehicle_base</b> - stores all itself a class, which in its turn has all necessary functions to work with the car database
+ <b>tests_drivers</b> - file tests driver database. At the moment it does not work because of the moved database
+ <b>vehicle_test</b> - test file for the vehicle database. Not working at the moment due to relocated database
________________________
## How to find the code that sends the messages? 

### First, you should understand what heandler, FSMstate, Command are. 
+ <b>Heandler</b> is a telegram function which reacts to some request, processes it and outputs the result. 
+ <b>FSMstate</b> is a function that helps to react on messages sent after heandler.
+ <b>Command("...")</b> is a filter for commands

Example code 


```python
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
```
Useful links:
#### https://core.telegram.org/bots/api#user - site with all Telegram APIs

#### To find the files you need to go to the following path: <i>"Yalantis_homework\handlers\users"</i> 
<img src="screenshots\handler_path.jpg" width="300">

#### There are many files in this folder, the name of which explains what it is for. 

<b>!Important!</b>

#### It is not desirable to touch, modify and even more to delete file __init__.
<b>NOTHING WILL WORK.</b>
________
## How to find keyboards?

### There are two types of keypads in Telegram.
1. A <b>simple keypad</b>, this is highlighted at the bottom of the message entry bar.
2. The <b>attached keypad</b> is attached to a specific message.  
   
### Example code for the attached keyboard 
``` python
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
```

### Example code for the simple keyboard
``` python
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

```
#### For a full understanding, read what callback_data is and how it works in Telegram

#### To find the files you need to go to the following path: <i>"Yalantis_homework\keyboards"</i>
<img src="screenshots\keyboard_path.jpg" width="300">

#### The inline default folders contain keypad files and the __init__ package installer. The inline folder also contains the file with the callback_data installation functions
_______
## How to start the bot?
#### <B>!PERFORM STRICTLY IN ORDER!</b>
#### To run the bot you need to have.
1. a bot token (if you don't have one, you need to create one using Telegram bot: BotFather)
2. Your id (optional)
3. change your .env.dist file to .env
4. Fill in the instructions in the .env file
5. ! Run the file app.py! 
 <img src="screenshots\file.jpg" width="300">
 __________