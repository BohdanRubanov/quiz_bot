from aiogram.fsm.state import StatesGroup, State

class Registration(StatesGroup):
    name = State()
    phone_number = State()

class Teacher(StatesGroup):
    choise = State()
    questions_count = State()
    questions = State()
