from .settings import dispatcher
from aiogram.types import CallbackQuery
from .work_json import json_data, save_data
@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery):
    await callback.answer(text="button pressed")
    callback_data = callback.data.split("/")

    if callback_data[0] == "delete_test":
        users_data = json_data()
        user_data: dict = users_data[f"{callback.from_user.id}"]
        tests: list = user_data["test_list"]
        tests.pop(int(callback_data[1]))
        user_data["test_list"] = tests
        users_data[f"{callback.from_user.id}"] = user_data
        save_data(users_data)
        await callback.message.answer(text=f"Ви видалили тест №{int(callback_data[1]) + 1}") 
