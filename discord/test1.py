# bot.py
import os
import sys
import random
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = sys.argv[1]
print(TOKEN)

DM_USER = "Crandall#9893"
print(f'DMs going to: {DM_USER}')
DM_ID = 713480526631272588

# ** *******************************************************************
client = discord.Client(intents=discord.Intents.default())

async def looper():
    for i in range(5):
        print("hello")
        await asyncio.sleep(1)
        print("... World!")
        user = await client.fetch_user(713480526631272588)
        await user.send("Hello")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    user = await client.fetch_user(713480526631272588)
    print('user:',user)
    await user.send("on_ready() launched")

    # asyncio.to_thread(looper) # Only works in Python 3.9+

    print("Looper launched")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.author.id)

    user = await client.fetch_user(713480526631272588)
    print('user:',user)
    await user.send("Hello")


    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)
