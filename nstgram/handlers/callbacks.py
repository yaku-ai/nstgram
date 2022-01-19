import wget

from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher

from nstgram import constants, bot, API_TOKEN
from nstgram.keyboards import confirm_keyboard, style_keyboard
from nstgram.states.user import SpecificStyle

from nstgram.model import style_transfer


# @dp.callback_query_handler(
#     lambda callback: callback.data in constants.STYLES,
#     state=SpecificStyle.algorithm_state
# )
async def select_style_handler(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await SpecificStyle.result_state.set()
    async with state.proxy() as data:
        data['style'] = callback.data
        await callback.message.edit_text('Подтвердите ваш выбор', reply_markup=confirm_keyboard(data['style']))


# @dp.callback_query_handler(
#     lambda callback: callback.data == 'Назад',
#     state=SpecificStyle.result_state
# )
async def back_cmd_handler(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await SpecificStyle.algorithm_state.set()
    async with state.proxy() as data:
        del data['style']
    await callback.message.edit_text('Выберите стиль для изображения', reply_markup=style_keyboard())


# @dp.callback_query_handler(
#     lambda callback: callback.data.startswith('apply'),
#     state=SpecificStyle.result_state
# )
async def ready_style_selected_handler(
    callback: types.CallbackQuery,
    state: FSMContext
):
    async with state.proxy() as data:
        result: types.File = await bot.get_file(data['content'])
        id = callback.message.chat.id
        file_path = f'/home/yakuai/YakuWS/nstgram/nstgram/model/data/{data["content"]}_{id}.png'
        wget.download(f"https://api.telegram.org/file/bot{API_TOKEN}/{result.file_path}", file_path)
        await callback.message.edit_text('Ждите применяется перенос стиля', reply_markup=None)
        style_transfer(file_path, callback.message.chat.id, data['content'], data['style'].lower())
        await callback.bot.send_photo(callback.message.chat.id,
                                      photo=open(f'/home/yakuai/YakuWS/nstgram/nstgram/model/data/result_'
                                                 f'{data["content"]}_{id}.png', 'rb'))




def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(select_style_handler, lambda callback: callback.data in constants.STYLES,
                                       state=SpecificStyle.algorithm_state)
    dp.register_callback_query_handler(back_cmd_handler, lambda callback: callback.data.startswith('Вернуться'),
                                       state=SpecificStyle.result_state)
    dp.register_callback_query_handler(ready_style_selected_handler, lambda callback: callback.data.startswith('Применить'),
                                       state=SpecificStyle.result_state)
