from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda message: message.text == "🎁 Daily Bonus")
async def daily_handler(message: Message):
    await message.answer(
        "🎁 Tabriklaymiz!\n\n"
        "Siz 100 coin oldingiz."
    )
