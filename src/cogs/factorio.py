# src/cogs/factorio.py
import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
class Factorio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_start_url = os.getenv('API_START_FACTORIO_URL')
        self.api_stop_url = os.getenv('API_STOP_FACTORIO_URL')
        self.headers = {"x-api-key": os.getenv("AWS_API_GATEWAY_KEY")}

    @commands.command(name='start_factorio', help='Starts the Factorio server')
    async def start_server(self, ctx):
        await ctx.send("Invoking Lambda function to start the Factorio server...")
        try:
            response = requests.post(self.api_start_url, headers=self.headers)
            if response.status_code == 200:
                await ctx.send("EC2 server starting.")
            else:
                await ctx.send(f"Failed to start Factorio server: {response.text}")
        except Exception as e:
            await ctx.send(f"Error: {e}")

    @commands.command(name='stop_factorio', help='Stops the Factorio server')
    async def stop_server(self, ctx):
        await ctx.send("Invoking Lambda function to stop the Factorio server...")
        try:
            response = requests.post(self.api_stop_url, headers=self.headers)
            if response.status_code == 200:
                await ctx.send("EC2 server stopping.")
            else:
                await ctx.send(f"Failed to stop Factorio server: {response.text}")
        except Exception as e:
            await ctx.send(f"Error: {e}")
            
# Command to check the Factorio server status
    @commands.command(name='status_factorio', help='Displays the Factorio server status')
    async def server_status(self, ctx):
        await ctx.send("Checking Factorio server status...")
        # Placeholder: Add logic to check the server’s status
        # Example responses based on server state
        # "The Factorio server is currently running. IP: 123.456.78.90, Port: 34197"
        await ctx.send("Factorio server is currently running!")  # Placeholder response
           
async def setup(bot):
    await bot.add_cog(Factorio(bot))

async def setup(bot):
    await bot.add_cog(Factorio(bot))
