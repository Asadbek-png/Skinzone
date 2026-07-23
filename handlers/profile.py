from telegram import Update
from telegram.ext import ContextTypes

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 Profil\n\n💰 Balans: 0"
    )
