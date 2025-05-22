import discord
from discord.ext import commands
import os
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
async def setup(bot):
    await bot.load_extension("nsfw")
    await bot.load_extension("anime")


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs (NSFW commands)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()

@bot.event
async def setup_hook():
    await bot.load_extension("commands.nsfw")

bot.run(TOKEN)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Serving Degens"))

# Load all command files (cogs)
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('YOUR_BOT_TOKEN')
