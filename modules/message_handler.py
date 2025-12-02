from .settings import dispatcher
from aiogram.types import Message
from .work_json import json_data
from aiogram.fsm.context import FSMContext
from .states import Registration
@dispatcher.message()
async def message_handler(message: Message, state: FSMContext):
    if message.text == "Вчитель":
        users_data = json_data()
        if message.from_user.id in users_data:
            await message.answer(text="Ви вже зареєстровані")
        else:
            await state.set_state(Registration.name)
            await message.answer(text="Потрібно зареєструватися. Введіть своє ім'я")
