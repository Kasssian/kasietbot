from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, admins
import random


async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько планет в солнечной системе?"
    answers = [
        '7',
        '8',
        '9',
        '10',
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Иди учи астрономию",
        reply_markup=markup
    )


async def mem(message: types.Message):
    mems = [
        'Mems/images.jpg',
        'Mems/images (1).jpg'
    ]
    mem = open(random.choice(mems), 'rb')
    await bot.send_photo(message.chat.id, photo=mem)


async def emoji(message: types.Message):
    if message.from_user.id in admins and message.text.startswith('game'):
        game = random.choice('⚽ 🏀 🎲 🎳 🎯 🎰'.split())
        await bot.send_dice(message.chat.id, emoji=game)


async def dice_game(message: types.Message):
    bot_dice = await bot.send_dice(message.chat.id)
    user_dice = await bot.send_dice(message.chat.id)
    await message.answer("первый игральный кость бота а второй игрока")
    if bot_dice.dice.value > user_dice.dice.value:
        await message.answer(f"Бот выиграл {message.from_user.full_name}!")
    elif bot_dice.dice.value == user_dice.dice.value:
        await message.answer("Ничья")
    else:
        await message.answer(f"{message.from_user.full_name} выиграл бота!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(start, commands=["start", 'info'])
    dp.register_message_handler(dice_game, commands=['dice'])
    dp.register_message_handler(emoji)