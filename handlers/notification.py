import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Будет сделано!")


async def go_to_patty():
    await bot.send_message(chat_id=chat_id, text="Сегодня в 13:00 в Geektech будет пицца!")


async def scheduler():
    aioschedule.every().sunday.at('11:00').do(go_to_patty())
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_id, lambda word: "напомни" in word.text)