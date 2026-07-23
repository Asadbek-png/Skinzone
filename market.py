from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def market(message: Message):
    if message.text == "🛒 Market":
        await message.answer("🛒 Market tez orada ishga tushadi.")
