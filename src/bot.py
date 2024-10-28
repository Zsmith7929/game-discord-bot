import discord
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