from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def inventory(message: Message):
    if message.text == "🎒 Inventory":
        await message.answer("🎒 Inventaringiz hozircha bo'sh.")
