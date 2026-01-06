from .settings import dispatcher
from aiogram.types import Message
from .work_json import json_data
from aiogram.fsm.context import FSMContext
from .states import Registration, Teacher
from .buttons import teacher_buttons
@dispatcher.message()
async def message_handler(message: Message, state: FSMContext):
    if message.text == "Вчитель":
        users_data = json_data(file_name="users.json")
        if str(message.from_user.id) in users_data:
            await message.answer(text="Оберіть дію", reply_markup=teacher_buttons())
            await state.set_state(Teacher.choise)
        else:
            await state.set_state(Registration.name)
            await message.answer(text="Потрібно зареєструватися. Введіть своє ім'я")
