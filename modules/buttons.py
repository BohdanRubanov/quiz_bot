from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
def start_buttons():
    button1 = KeyboardButton(text="Вчитель")
    button2 = KeyboardButton(text="Учень")
    list_buttons = [
        [button1, button2],
    ]
    markup = ReplyKeyboardMarkup(keyboard=list_buttons, resize_keyboard=True)
    return markup

def teacher_buttons():
    button1 = KeyboardButton(text="Створити тест")
    button2 = KeyboardButton(text="Видалити тест")
    button3 = KeyboardButton(text="Переглянути мої тести")
    list_buttons = [
        [button1],
        [button2],
        [button3]
    ]
    markup = ReplyKeyboardMarkup(keyboard=list_buttons, resize_keyboard=True)
    return markup
    
def endtest_buttons():
    button1 = KeyboardButton(text="Завершити створення тесту")
    list_buttons = [
        [button1]
    ]
    markup = ReplyKeyboardMarkup(keyboard=list_buttons, resize_keyboard=True)
    return markup

def test_buttons(test_index:int):
    button1 = InlineKeyboardButton(text= "Отримати код", callback_data= f"get_code/{test_index}")
    button2 = InlineKeyboardButton(text= "Видалити тест", callback_data= f"delete_test/{test_index}")
    list_buttons = [
        [button1],
        [button2]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=list_buttons)
    return markup 

def start_button(code:int):
    button = InlineKeyboardButton(text="Розпочати тест", callback_data=f"start_test/{code}")
    list_buttons = [
        [button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=list_buttons)
    return markup 

def next_question(question_index: int, code: int):
    button = InlineKeyboardButton(text="Наступне питання", callback_data=f"next_question/{code}/{question_index}")
    list_buttons = [
        [button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=list_buttons)
    return markup 
def end_test(code:int):
    button = InlineKeyboardButton(text="Завершити тест", callback_data=f"end_test/{code}")
    list_buttons = [
        [button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=list_buttons)
    return markup 