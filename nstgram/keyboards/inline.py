from aiogram import types

from nstgram import constants


def style_keyboard() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=2)
    for style_name in constants.STYLES:
        markup.add(
            types.InlineKeyboardButton(
                style_name,
                callback_data=style_name)
        )
    return markup


def confirm_keyboard(style_name: str) -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=2)
    for button_name in [f"Применить {style_name} стиль", 'Вернуться назад']:
        markup.add(
            types.InlineKeyboardButton(
                button_name,
                callback_data=button_name)
        )
    return markup


