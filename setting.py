from aiogram import Bot, Dispatcher
from decouple import config

token = config('TOKEN')

bot = Bot(token)
dp = Dispatcher(bot=bot)
admins = [938358138]
