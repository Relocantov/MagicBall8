import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router  # Импортируем обработчик из handlers.py

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем .env файл

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("TOKEN не загружен! Проверь переменные окружения.")

bot = Bot(token=TOKEN)

# Создание бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    import os
from aiogram import Bot, Dispatcher
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    port = os.getenv("PORT", 8080)  # Render требует PORT
    asyncio.run(main())