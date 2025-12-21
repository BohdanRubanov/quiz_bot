from .settings import dispatcher
from .states import Registration, Teacher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from .work_json import json_data, save_data
from .buttons import endtest_buttons

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
    await state.clear()

@dispatcher.message(Teacher.choise)
async def choise_handler(message: Message, state: FSMContext):
    if message.text == "Створити тест":
        await state.set_state(Teacher.questions_count)
        await message.answer(text= "Введіть кількість питань")

    
@dispatcher.message(Teacher.questions_count)
async def questions_count_handler(message: Message, state: FSMContext):
    await state.update_data(questions_count = message.text)
    await state.update_data(questions = [])
    await state.set_state(Teacher.questions)
    # await message.answer(text="Питання потрібно вводити у відповідному вигляді:\n Номер питання. Текст питання \n Приклад:\n 1. Скільки буде 2+2?")
    await message.answer(text="Введіть перше питання")

@dispatcher.message(Teacher.questions)
async def questions_handler(message: Message, state: FSMContext):
    await state.update_data(options = [])
    state_data = await state.get_data()
    await state.set_state(Teacher.options)
    
    if int(state_data["questions_count"]) > len(state_data["questions"]):
        await message.answer(text="Введіть варіанти відповідей")
        question_data = {
            "text": message.text,
            "options": state_data["options"]
        }
        questions_list:list = state_data["questions"]
        questions_list.append(question_data)
        await state.update_data(questions = questions_list)
        
    else:
        test_data = await state.get_data()
        user_json_data = json_data()
        user = user_json_data[f"{message.from_user.id}"]
        user["test_list"].append(test_data["questions"])
        user_json_data[f"{message.from_user.id}"] = user
        save_data(user_json_data)
        await message.answer(text= "Тест успішно збережено")
        await state.clear()
        
@dispatcher.message(Teacher.options)
async def options_handler(message: Message, state: FSMContext):
    state_data = await state.get_data()
    if 3 > len(state_data["options"]):
        options_list:list = state_data["options"]
        options_list.append(message.text)
        await state.update_data(options = options_list)
        await message.answer(text= "Варіант відповіді збережено. Введіть наступний: ")
    else:
        options_list:list = state_data["options"]
        options_list.append(message.text)
        await state.update_data(options = options_list)
        await state.set_state(Teacher.questions)
        if int(state_data["questions_count"]) > len(state_data["questions"]):
            await message.answer(text= "Питання збережено. Введіть наступне: ")
        else:
            await message.answer(
                text= "Ви ввели всі питання. Натисніть на кнопку для завершення створення тесту",
                reply_markup= endtest_buttons()
            )
        
