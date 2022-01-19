from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram import types
from aiogram.types.message import ContentType

from nstgram import bot
from nstgram.keyboards import style_keyboard
from nstgram.states.user import SpecificStyle


# @dp.message_handler(commands='start', state="*")
async def cm_start(message: types.Message):
    await SpecificStyle.content_state.set()
    await bot.send_message(
        message.chat.id,
        "Загрузите изображение для стилизации"
    )


# @dp.message_handler(content_types=['photo'], state=SpecificStyle.content_state)
async def load_content(message: types.Message, state: FSMContext):
    await SpecificStyle.algorithm_state.set()
    async with state.proxy() as data:
        if message.document:
            data['content'] = message.document.file_id
        elif message.photo:
            data['content'] = message.photo[0].file_id
    await message.reply(
        'Выберите стиль для изображения',
        reply_markup=style_keyboard()
    )


def register_user_handler(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state="*")
    dp.register_message_handler(load_content, content_types=[ContentType.PHOTO, ContentType.DOCUMENT],
                                state=SpecificStyle.content_state)
