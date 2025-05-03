from keep_alive import keep_alive

keep_alive()

import discord
import requests
import json
import os  # <- para pegar o token de ambiente

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Pega o token do ambiente
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN is None:
    print("Erro: variável de ambiente DISCORD_BOT_TOKEN não encontrada.")
else:
    client.run(TOKEN)

