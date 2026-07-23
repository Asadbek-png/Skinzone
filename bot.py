
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.profile import router as profile_router
from handlers.daily import router as daily_router
from handlers.case import router as case_router

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(daily_router)
    dp.include_router(case_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
