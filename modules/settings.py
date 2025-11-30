from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("TOKEN")

bot = Bot(token=token)
dispatcher = Dispatcher()