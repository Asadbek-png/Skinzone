from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def bonus(message: Message):
    if message.text == "🎁 Daily Bonus":
        await message.answer("🎁 Siz 100 coin oldingiz!")
