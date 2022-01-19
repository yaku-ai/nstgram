from aiogram.dispatcher.filters.state import State, StatesGroup


class SpecificStyle(StatesGroup):
    content_state = State()
    algorithm_state = State()
    result_state = State()


class CustomStyle(StatesGroup):
    content_state = State()
    algorithm_state = State()
    style_state = State()
    additional_style_state = State()
    result_state = State()

