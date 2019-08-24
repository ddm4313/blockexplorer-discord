import discord
import re
import requests
from blockcypher import get_transaction_details

class Bot(discord.Client):
    async def on_ready(self):
        print(f"Authenticated: {self.user}")
    async def on_message(self, message):
        if "!txid" in message.content:
            message_tx = re.search("(?<=!txid)(.*)", message.content)
            tx_id = message_tx[0].replace(" ", "")
            btc_info = get_transaction_details(tx_id)
            tx_amount = btc_info['total']
            price = requests.get("https://blockchain.info/q/24hrprice")
            await message.channel.send(f"TXID: {tx_id} | Confirmations: {btc_info['confirmations']} | Date: {btc_info['received']} | Bitcoin Price (USD): {price.text}")
client = Bot()
client.run('token')
