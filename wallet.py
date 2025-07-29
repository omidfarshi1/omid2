from solana.rpc.async_api import AsyncClient
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.publickey import PublicKey
from solana.rpc.commitment import Confirmed
import asyncio
from config import Config

class Wallet:
    def __init__(self, seed_phrase):
        self.keypair = Keypair.from_seed_phrase(seed_phrase)  # فرضی، برای نمونه
        self.client = AsyncClient("https://api.mainnet-beta.solana.com")

    async def send_sol(self, to_pubkey: PublicKey, lamports: int):
        txn = Transaction()
        txn.add(transfer(TransferParams(from_pubkey=self.keypair.public_key, to_pubkey=to_pubkey, lamports=lamports)))
        resp = await self.client.send_transaction(txn, self.keypair)
        await self.client.confirm_transaction(resp['result'])
        return resp