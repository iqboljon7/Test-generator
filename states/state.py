from aiogram.fsm.state import State, StatesGroup

class add_tests(StatesGroup):
    get_tests = State()
    get_numbers = State()
    get_answers = State()