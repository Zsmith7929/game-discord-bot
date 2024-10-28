import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content

# Set up bot with command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Example command
@bot.command(name='start', help='Starts the Factorio server')
async def start_server(ctx):
    await ctx.send("Starting the Factorio server...")

@bot.command(name='stop', help='Stops the Factorio server')
async def stop_server(ctx):
    await ctx.send("Stopping the Factorio server...")

# Run the bot with token
bot.run(TOKEN)
