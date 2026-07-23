from aiogram import Router
from aiogram.types import Message
from utils import open_case

router = Router()

@router.message(lambda message: message.text == "🎲 Case")
async def case_handler(message: Message):
    skin, price = open_case()
    await message.answer(
        f"🎲 Sizga tushdi:\n\n"
        f"🔫 {skin}\n"
        f"💰 Qiymati: {price} coin"
    )
