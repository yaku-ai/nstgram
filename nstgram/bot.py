from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from create_bot import dp
from handlers import client


import os


client.register_handler_client(dp)


async def on_startup(_):
    print('bot is active')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




