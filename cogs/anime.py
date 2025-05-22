import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def waifu(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.waifu.pics/sfw/waifu') as resp:
                data = await resp.json()
                await ctx.send(data['url'])

    @commands.command()
    async def neko(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.waifu.pics/sfw/neko') as resp:
                data = await resp.json()
                await ctx.send(data['url'])

    @commands.command()
    async def hug(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.waifu.pics/sfw/hug') as resp:
                data = await resp.json()
                await ctx.send(data['url'])

    @commands.command()
    async def pat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.waifu.pics/sfw/pat') as resp:
                data = await resp.json()
                await ctx.send(data['url'])

def setup(bot):
    bot.add_cog(Anime(bot))
