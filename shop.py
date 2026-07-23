from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def shop(message: Message):
    if message.text == "🛒 Shop":
        await message.answer("🛒 Shop tez orada qo'shiladi.")
