import os
import logging
from aiogram import Bot, Dispatcher, types
import asyncio
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)

# Создание бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я Telegram-бот!")

if __name__ == "__main__":
  async def main():
    await dp.start_polling(bot)

asyncio.run(main())