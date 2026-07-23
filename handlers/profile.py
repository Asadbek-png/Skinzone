from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda message: message.text == "👤 Profil")
async def profile_handler(message: Message):
    await message.answer(
        "👤 Profil\n\n"
        "💰 Balans: 0 coin\n"
        "🎁 Daily bonus: Mavjud"
    )
