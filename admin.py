from aiogram import Router
from aiogram.types import Message
from config import ADMIN_ID

router = Router()

@router.message()
async def admin(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👑 Admin panel")
