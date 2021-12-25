from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.drivers_base import DriverDataBase
from utils.db_api.vehicle_base import VehicleDataBase

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

vdb = VehicleDataBase()
dbd = DriverDataBase()
