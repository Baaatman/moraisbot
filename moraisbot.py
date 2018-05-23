import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import random
import re

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

classico = ["moderno", "contemporâneo"]
antesFosse = ["pois fosse", "depois fosse"]

@client.event
async def on_ready():
    print("Bot ready!")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    newMessage = message.content
    messageChanged = False

    if "CLASSICO" in message.content.upper():
        replacement = classico[random.randint(0, 1)]
        replaceClassico = re.compile(re.escape('classico'), re.IGNORECASE)
        newMessage = replaceClassico.sub(replacement, newMessage)
        messageChanged = True

    if "ANTES FOSSE" in message.content.upper():
        replacement = antesFosse[random.randint(0, 1)]
        replaceAntesFosse = re.compile(re.escape('antes fosse'), re.IGNORECASE)
        newMessage = replaceAntesFosse.sub(replacement, newMessage)
        messageChanged = True

    if messageChanged:
        await client.send_message(message.channel, newMessage)

client.run("NDQ4MTAyMjY1MzMzNzQzNjI2.DeRQqw.Mz9WEB9F6EaOKYKjFcUrl-twqn0")