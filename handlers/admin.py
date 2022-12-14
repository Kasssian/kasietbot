from aiogram import types, Dispatcher
from config import bot


async def zak(message: types.Message):
    if not message.reply_to_message:
        await message.answer('Отправь как ответ')
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(zak, commands=['pin'], commands_prefix='!')
