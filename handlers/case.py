from telegram import Update
from telegram.ext import ContextTypes
from utils import open_case

async def case(update: Update, context: ContextTypes.DEFAULT_TYPE):
    skin, price = open_case()
    await update.message.reply_text(
        f"🎲 Sizga tushdi:\n\n🔫 {skin}\n💰 Qiymati: {price} coin"
    )
