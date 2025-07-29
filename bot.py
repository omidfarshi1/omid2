from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import Config

class TelegramBot:
    def __init__(self, wallet, monitor):
        self.wallet = wallet
        self.monitor = monitor
        self.app = ApplicationBuilder().token(Config.TELEGRAM_TOKEN).build()
        self.app.add_handler(CommandHandler("start", self.start_command))
        # دستورات دیگر اینجا

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("ربات کپی‌ترید فعال شد!")

    async def start(self):
        await self.app.run_polling()