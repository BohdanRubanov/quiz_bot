from aiogram.fsm.state import StatesGroup, State

class Registration(StatesGroup):
    name = State()
    phone_number = State()

class Teacher(StatesGroup):
    choise = State()
    questions_count = State()
    questions = State()
    options = State()



# {
#     "test_list": [
#         [
#            {
#                "text": "2+2=?",
#                "options": ["3", "5", "4", "8"],
#                "correct_option": "4"
#            },
#            {
#                "text": "2+2=?",
#                "options": ["3", "5", "4", "8"],
#                "correct_option": "4"
#            },
#         ]
#     ]
# }