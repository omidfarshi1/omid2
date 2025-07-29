import asyncio
from monitor import Monitor
from bot import TelegramBot
from wallet import Wallet
from config import Config

async def main():
    wallet = Wallet(Config.SEED_PHRASE)
    monitor = Monitor(Config.WHALE_ADDRESS, wallet)
    bot = TelegramBot(wallet, monitor)
    await asyncio.gather(
        monitor.start(),
        bot.start()
    )

if __name__ == "__main__":
    asyncio.run(main())