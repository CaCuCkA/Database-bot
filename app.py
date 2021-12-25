from aiogram import executor

from loader import dp
from loader import vdb, dbd
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

try:
    dbd.create_drivers_table()
except Exception as error:
    print(error)
print(dbd.select_all_drivers())

try:
    vdb.create_vehicle_table()
except Exception as error:
    print(error)
print(vdb.select_all_vehicles())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

