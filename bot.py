# importing built in modules
import string
from os.path import join, dirname
import os
import json
import asyncio
import random
from threading import Thread
import platform
import uuid 

# import third party modules
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import aiohttp
from pycoingecko import CoinGeckoAPI
import jishaku
import topgg
import motor
from discord_slash import SlashCommand
import discord_slash
from aiohttp.resolver import AsyncResolver
from flask import Flask
import psutil
loop = asyncio.get_event_loop()
import asyncio
cg = CoinGeckoAPI()
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
intents = discord.Intents.default()

token = os.getenv("token")
dbltoken = os.getenv("dbltoken")



bot = commands.Bot(command_prefix=commands.when_mentioned_or("ta!!"), intents=intents)
slash = SlashCommand(bot, sync_commands=True)


bot.remove_command("help")
# bot.load_extension("safeeval")
bot.load_extension("jishaku")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
        print(f"loaded: cogs.{name}")

async def ch_pr():
    await bot.wait_until_ready()
    await asyncio.sleep(30)
    while True:
        await asyncio.sleep(30) # waits for init
        statuss = ["prefix : ta!!","made with python3 lol","0xf667485f542185d2c27B897E660a589a37b21FCc my ethereum adress dont forget to donate :D ",
        "made by takipsizad",f"on {len(bot.guilds)} servers","ta!!help for help",f"on {round(bot.latency * 1000)} ping",f"discord py version: {(discord.__version__)}",
        "ta!!vote :D ","bc1q4us2ueuayl4j36ju708xzez7vdpurpw33n8amv my bitcoin adress dont forget to donate :D ","dont forget to donate :D ",
        "hey idk what to write","slash commands are out ","never gonna give you up let you down run around and desert you","hey there thanks to you for using my bots","h",
        ":D ","ಠ_ಠ","7/24 online lol","aiohttp included","[insert list]","ta!!help help command","no requests included","database included","mongo db included" "LOL","running python","python included",
        "bored","slash commands are out ","""Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed""""i run out of ideas",
        ":D","h","not made with node.js","made by takipsizad#1919 / 9999","the developer of this bot is available for hire | dm on discord takipsizad#1919 / 9999",f"made with {platform.python_implementation()}",
        "random things go","i hate c++ WHAT İS cout <<string","bruh","c is better then c++ change my mind","idk lol" "sike","eeee",
        "batteries included","no setup needed","gas gas gas","random things go ","smh","prinf() > cout <<","(¬_¬)"," this bot wont get verified","Usb stick",
        "discord moment","powered by discord.py","discord.py included ","just invite the bot to setup","dont watch my status",
        "l","bored","i am bored but idk","🏳️‍⚧️ transgender rights are human rights","no homophobia permitted","discord pls open my account and not give me pain"]
        statusss = discord.Game(random.choice(statuss))
        await bot.change_presence(
            status=discord.Status.do_not_disturb, activity=statusss, afk=True
        )

@bot.command()
async def cryptoprices(ctx, arg1, arg2):
    prices = cg.get_price(ids=arg1, vs_currencies=arg2)
    p2 = prices[arg1]
    e = p2[arg2]
    embed = discord.Embed()
    embed.add_field(name=f"{arg1} prices", value=f"{arg1} price: {e} in {arg2}")
    await ctx.reply(f"{arg1} price: {e} in {arg2}")

app = Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

#Thread(target=app.run, args=("0.0.0.0", 8080)).start()
bot.loop.create_task(ch_pr())
Thread(target=bot.run(token)).start()