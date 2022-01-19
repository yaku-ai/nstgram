from aiogram import types
from aiogram.dispatcher import Dispatcher

dp = Dispatcher()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    pass


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.message):
    pass


