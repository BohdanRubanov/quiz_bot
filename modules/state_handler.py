from .settings import dispatcher
from .states import Registration
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from .work_json import json_data, save_data

@dispatcher.message(Registration.name)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await state.set_state(Registration.phone_number)
    await message.answer(text="Введіть свій номер телефону")

@dispatcher.message(Registration.phone_number)
async def number_handler(message: Message, state: FSMContext):
    await state.update_data(phone_number= message.text)
    user_data = await state.get_data()
    user_json_data = json_data()
    user_json_data.setdefault(
        message.from_user.id, 
        {
            "name": user_data["name"],
            "phone_number": user_data["phone_number"],
            "test_list": []
        }
    )
    save_data(user_json_data)
    await message.answer(text="Реєстрація успішна")
    