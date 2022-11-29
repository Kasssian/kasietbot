from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import admins
from keyboards.keyboards import cancel_markup, submit_markup
from database.db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in admins:
        await FSMAdmin.id.set()
        await message.answer('id')


    else:
        await message.answer("Пиши в личку!")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = int(message.text)
    await FSMAdmin.next()
    await message.answer("name?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("НАПРАВЛЕНИЕ?")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("возраст?")


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAdmin.next()
    await message.answer("групаа?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group_'] = message.text
    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # Запись в БД
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Все свободен!")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer("Повторите")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена")


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
