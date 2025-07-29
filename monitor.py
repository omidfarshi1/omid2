import asyncio
from solana.rpc.websocket_api import connect
from config import Config

class Monitor:
    def __init__(self, whale_address, wallet):
        self.whale_address = whale_address
        self.wallet = wallet
        self.subscribed = False

    async def start(self):
        async with connect("wss://api.mainnet-beta.solana.com/") as websocket:
            await websocket.logs_subscribe(filters=[{"mentions": [self.whale_address]}])
            self.subscribed = True
            while True:
                msg = await websocket.recv()
                print("New log:", msg)
                # تحلیل تراکنش و خرید خودکار اینجا