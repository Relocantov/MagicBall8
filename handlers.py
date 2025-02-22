from aiogram import Router, types

router = Router()

@router.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я Telegram-бот!")