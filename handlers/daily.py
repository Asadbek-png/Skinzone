from telegram import Update
from telegram.ext import ContextTypes

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎁 Kunlik bonus: +100 coin"
    )
