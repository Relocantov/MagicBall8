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