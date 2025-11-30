from modules import bot, dispatcher
import asyncio

async def main():
    await dispatcher.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

