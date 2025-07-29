from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from wallet import Wallet

TOKEN = "8124214114:AAFEzLjQ-WtMX7BfCUQPpr9qwzjig6FNkgg"
WALLET_SEED = "success romance web pretty risk mouse multiply permit waste orbit car autumn"
COPY_TRADE_AMOUNT = 0.01
WHALE_ADDRESS = "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"

wallet = Wallet(WALLET_SEED)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات کپی‌ترید فعال است!")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sol = wallet.get_balance()
    await update.message.reply_text(f"موجودی: {sol} SOL")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.run_polling()
