from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎁 Daily Bonus"),
            KeyboardButton(text="🎲 Case")
        ],
        [
            KeyboardButton(text="👤 Profil"),
            KeyboardButton(text="🛒 Market")
        ]
    ],
    resize_keyboard=True
)
