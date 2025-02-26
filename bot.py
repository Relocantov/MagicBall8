import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import F
from dotenv import load_dotenv
from handlers import router  # Импортируем обработчик из handlers.py

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Проверяем, загружен ли токен
if not TOKEN:
    raise ValueError("TOKEN не загружен! Проверь переменные окружения.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(router)

# Добавляем обработчик команды "Привет!"
@dp.message(F.text == "Привет!")
async def hello_message(message: types.Message):
    await message.answer("Привет! 😊")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())