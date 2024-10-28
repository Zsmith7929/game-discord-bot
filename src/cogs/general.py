# src/cogs/general.py
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Responds with pong')
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(General(bot))
