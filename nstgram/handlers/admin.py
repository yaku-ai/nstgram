from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class FSM(StatesGroup):
    content_state = State()
    algorithm_state = State()
    style_state = State()
    # additional_style_state = State()
    result_state = State()


@dp.message_handler(commands='load', state=None)
async def cm_start(message: types.Message):
    await FSM.content_state.set()
    await message.reply('load content')


@dp.message_handler(content_types=['photo'], state=FSM.content_state)
async def load_content(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM.next()
    await message.reply('something')
