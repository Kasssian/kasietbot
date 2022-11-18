from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('TOKEN')

storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(bot=bot, storage=storage)
admins = [938358138]
