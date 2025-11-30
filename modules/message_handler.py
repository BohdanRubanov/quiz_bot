from .settings import dispatcher
from aiogram.types import Message
from .work_json import json_data, save_data
@dispatcher.message()
async def message_handler(message: Message):
    if message.text == "Вчитель":
        users_data = json_data()
        if message.from_user.id in users_data:
            await message.answer(text="Ви вже зареєстровані")
        else:
            await message.answer(text="Потрібно зареєструватися. Введіть своє ім'я та імейл")
    if "@" in message.text:
        user_data = message.text.split(" ")
        users_data = json_data()
        users_data[message.from_user.id] = user_data
        save_data(users_data)



