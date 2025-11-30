from .settings import dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from .buttons import start_buttons
@dispatcher.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(text=f"Привіт, {message.from_user.first_name} ! \nОберіть вашу роль", reply_markup=start_buttons())