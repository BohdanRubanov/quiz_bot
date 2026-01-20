from .settings import dispatcher
from aiogram.types import CallbackQuery
from .work_json import json_data, save_data
from .buttons import start_button
from .settings import bot
import random
@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery):
    await callback.answer(text="button pressed")
    callback_data = callback.data.split("/")
    if callback_data[0] == "delete_test":
        users_data = json_data(file_name="users.json")
        user_data: dict = users_data[f"{callback.from_user.id}"]
        tests: list = user_data["test_list"]
        tests.pop(int(callback_data[1]))
        user_data["test_list"] = tests
        users_data[f"{callback.from_user.id}"] = user_data
        save_data(file_name="users.json", data= users_data)
        await callback.message.answer(text=f"Ви видалили тест №{int(callback_data[1]) + 1}") 
    elif callback_data[0] == "get_code":
        code= random.randint(100000,999999)
        users_data = json_data(file_name="users.json")
        user_data: dict = users_data[f"{callback.from_user.id}"]
        tests: list = user_data["test_list"]
        active_test = tests[int(callback_data[1])]
        data_to_save = {
            "owner": f"{callback.from_user.id}",
            "test": active_test,
            "students": {}
        }
        active_tests_data = json_data(file_name="active_tests.json")
        active_tests_data.setdefault(f"{code}", data_to_save)
        save_data(file_name="active_tests.json", data=active_tests_data)
        await callback.message.answer(text=str(code), reply_markup= start_button(code))
    elif callback_data[0] == "start_test":
        active_tests = json_data(file_name="active_tests.json")
        current_test = active_tests[f"{callback_data[1]}"]
        questions = current_test["test"]
        question = questions[0]
        students: dict = current_test["students"]
        for key, value in students.items():
            await bot.send_message(chat_id= int(key), text= question["text"]) 
        await callback.message.answer(text= question["text"])