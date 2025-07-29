from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solders.pubkey import Pubkey
from solana.rpc.commitment import Confirmed
from solana.rpc.async_api import AsyncClient
from mnemonic import Mnemonic
import base58

class Wallet:
    def __init__(self, seed_phrase):
        self.client = Client("https://api.mainnet-beta.solana.com")
        mnemo = Mnemonic("english")
        seed = mnemo.to_seed(seed_phrase)
        self.keypair = Keypair.from_seed(seed[:32])

    def get_balance(self):
        return self.client.get_balance(self.keypair.public_key)["result"]["value"] / 1e9
