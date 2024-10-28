import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for guild in bot.guilds:
        print(f'Connected to server: {guild.name}')

# Automatically load all cogs in the 'cogs' directory
async def load_cogs():
    await bot.load_extension('cogs.general')
    await bot.load_extension('cogs.factorio')

# Run the bot
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# Run the main function
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
=======
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Define the bot and the command prefix
bot = commands.Bot(command_prefix='!')

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)
