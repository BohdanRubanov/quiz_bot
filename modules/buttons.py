from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
def start_buttons():
    button1 = KeyboardButton(text="Вчитель")
    button2 = KeyboardButton(text="Учень")
    list_buttons = [
        [button1, button2],
    ]
    markup = ReplyKeyboardMarkup(keyboard=list_buttons, resize_keyboard=True)
    return markup