from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
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