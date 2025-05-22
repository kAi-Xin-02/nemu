import discord
from discord import app_commands
from discord.ext import commands
import aiohttp
import os
import hmtai
from discord.ext import commands
import discord

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hentai(self, ctx):
        if not ctx.channel.is_nsfw():
            return await ctx.send("❌ This command can only be used in NSFW channels.")
        
        url = hmtai.use("neko", "hentai")
        embed = discord.Embed(title="Here's your hentai 🥵", color=discord.Color.dark_magenta())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def anal(self, ctx):
        if not ctx.channel.is_nsfw():
            return await ctx.send("❌ NSFW channel only!")
        
        url = hmtai.use("neko", "anal")
        embed = discord.Embed(title="Take this anal 💦", color=discord.Color.blurple())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def femdom(self, ctx):
        if not ctx.channel.is_nsfw():
            return await ctx.send("❌ This ain’t a playground, use in NSFW channels.")
        
        url = hmtai.use("neko", "femdom")
        embed = discord.Embed(title="Step on me, mommy 🖤", color=discord.Color.red())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(NSFW(bot))


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_image(self, endpoint):
        url = f"https://api.waifu.pics/nsfw/{endpoint}"  # Replace with your actual NSFW API
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data["url"]
                else:
                    return None

    async def send_nsfw(self, interaction, endpoint, title):
        if not interaction.channel.is_nsfw():
            await interaction.response.send_message("❌ This command can only be used in NSFW channels.", ephemeral=True)
            return

        image_url = await self.get_image(endpoint)
        if image_url:
            embed = discord.Embed(title=title, color=0xFF0055)
            embed.set_image(url=image_url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("❌ Failed to fetch image.", ephemeral=True)

    @app_commands.command(name="hentai", description="Send a random hentai image")
    async def hentai(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "waifu", "Here's your hentai, degenerate~")

    @app_commands.command(name="boobs", description="Send some boobs")
    async def boobs(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "boobs", "Enjoy these tiddies~")

    @app_commands.command(name="ass", description="Send an ass pic")
    async def ass(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "ass", "Cake time 🍑")

    @app_commands.command(name="ecchi", description="Send some ecchi art")
    async def ecchi(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "ecchi", "Lewd but not too lewd 👀")

    @app_commands.command(name="thighs", description="Thigh heaven")
    async def thighs(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "thighs", "Thicc thighs save lives~")

    @app_commands.command(name="waifu18", description="18+ Waifu content")
    async def waifu18(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "waifu", "NSFW waifu for you~")

    @app_commands.command(name="trap", description="Send a trap pic")
    async def trap(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "trap", "You sussy baka~")

    @app_commands.command(name="lewdneko", description="Lewd neko girl")
    async def lewdneko(self, interaction: discord.Interaction):
        await self.send_nsfw(interaction, "neko", "Meow~ here's your lewd neko")

async def setup(bot):
    await bot.add_cog(NSFW(bot))
