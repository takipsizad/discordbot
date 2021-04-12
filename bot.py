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
from bs4 import BeautifulSoup
from pytube import YouTube
import aiohttp
from pycoingecko import CoinGeckoAPI
import jishaku
import dbl
import motor
from discord_slash import SlashCommand
import discord_slash
from flask import Flask
import psutil
# importing local modules
import reddit
cg = CoinGeckoAPI()
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
ıntents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("ta!!"), intents=ıntents)
slash = SlashCommand(bot, sync_commands=True)
token = os.getenv("token")
dbltoken = os.getenv("dbltoken")
db = os.getenv("db")
client = motor.motor_tornado.MotorClient(db)
mydb = client["db"]
prmc = mydb.premiumcode
premium = mydb.premium
bot.remove_command("help")
bot.load_extension("help")
bot.load_extension("safeeval")
bot.load_extension("jishaku")


dble = dbl.DBLClient(bot=bot, token=dbltoken, autopost=True)


async def ch_pr():
    await bot.wait_until_ready()
    while True:
        statuss = ["prefix : ta!!","made with python3 lol","0xf667485f542185d2c27B897E660a589a37b21FCc my ethereum adress dont forget to donate :D ",
        "made by takipsizad",f"on {len(bot.guilds)} servers","ta!!help for help",f"on {round(bot.latency * 1000)} ping",f"discord py version: {(discord.__version__)}",
        "ta!!vote :D ","bc1q4us2ueuayl4j36ju708xzez7vdpurpw33n8amv my bitcoin adress dont forget to donate :D ","dont forget to donate :D ",
        "hey idk what to write","slash commands are out ","never gonna give you up let you down run around and desert you","hey there thanks to you for using my bots","h",
        ":D ","ಠ_ಠ","7/24 online lol","aiohttp included","[insert list]","ta!!help help command","no requests included","database included","mongo db included" "LOL","running python","python included",
        "bored","slash commands are out ","""Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed""""i run out of ideas",
        ":D","h","not made with node.js","made by takipsizad#1919","the developer of this bot is available for hire | dm on discord takipsizad#1919",f"made with {platform.python_implementation()}",
        "random things go","i hate c++ WHAT İS cout <<string","bruh","c is better then c++ change my mind","idk lol" "sike","eeee",
        "batteries included","no setup needed","gas gas gas","random things go ","smh","prinf() > cout <<","(¬_¬)"," this bot wont get verified","Usb stick",
        "discord moment","powered by discord.py","discord.py included ","just invite the bot to setup","dont watch my status",
            f"l","bored","i am bored but idk "
        ]
        statusss = discord.Game(random.choice(statuss))
        await bot.change_presence(
            status=discord.Status.do_not_disturb, activity=statusss
        )
        await asyncio.sleep(30)


@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong! In {round(bot.latency * 1000)}ms")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ipcheck(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.iplegit.com/info?ip={str(arg1)}",headers={"User-agent": "Mozilla/5.0"},) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["bad"]
            parsed_json3 = parsed_json["type"]
            parsed_json4 = parsed_json["ip"]
            await ctx.reply(f"bad: { str(parsed_json2)} type: {str(parsed_json3)} ip: {str(parsed_json4)}")


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def langdetect(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f"https://termsite.takipsizad.repl.co/api/langdetect?text={arg1}"),headers={"User-agent": "Mozilla/5.0"},) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json["lang"]
            await ctx.reply(f"language: {parsed_json2}")


@bot.command()
async def serverversion(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(("https://termsite.takipsizad.repl.co/api/serverversion"),headers={"User-agent": "Mozilla/5.0"}) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["serverversion"]
            await ctx.reply(f"server version {parsed_json2}")


@bot.command()
async def execute(ctx, *, args):
    if ctx.author.id == 542380989775740929:
        output = eval(args)
        await ctx.reply(output)
    else:
        raise commands.NotOwner("")

@bot.command()
async def devinfo(ctx):
    if ctx.author.id == 542380989775740929:
        mem = psutil.virtual_memory()
        await ctx.reply(f"""{mem}""")
    else:
        raise commands.NotOwner("")


@bot.command()
async def info(ctx):
    await ctx.reply(
        f"""
discord py version {discord.__version__}
aiohttp version  {aiohttp.__version__}
discord slash version  {discord_slash.__version__}
motor (mongodb) version  {motor.version}
os version {platform.platform(aliased=0, terse=0)}
python info {platform.python_implementation()} {platform.python_version()}
on {len(bot.guilds)} guilds 
made by takipsizad#1919"""
    )


@bot.event
async def on_guild_join(guild):
    await bot.wait_until_ready()
    channel = bot.get_channel(805355006551130122)
    await channel.send(f"i joined {guild}")


@bot.event
async def on_guild_remove(guild):
    await bot.wait_until_ready()
    channel = bot.get_channel(805355006551130122)
    await channel.send(f"i leaved {guild}")


@bot.command()
async def getwidget(ctx):
    await ctx.reply(await bot.fetch_widget(ctx.guild.id))


@bot.command(aliases=["create-invite", "createinvite"])
async def create_invite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.reply(f"Here is an instant invite to your server: {str(link)}")


@bot.command(aliases=["delete-invite", "delete_invite"])
@has_permissions(manage_guild=True)
async def deleteinvite(ctx, arg1):
    try:
        await bot.delete_invite(arg1)
        await ctx.reply("invite deleted")
    except:
        await ctx.reply("error deleting invite")


@bot.command()
async def echo(ctx, *, args):
    if not "@" in args:
        await ctx.send(args)
    else:
        await ctx.reply("dont send mentions")


@bot.command()
async def vote(ctx):
    embed = discord.Embed()
    embed.title = "Vote link"
    embed.add_field(
        name="vote link:",
        value="[vote](https://top.gg/bot/555036314077233172/vote?refferer=takipsizadbot)",
    )
    await ctx.reply(embed=embed)


@bot.command()
async def invite(ctx):
    embed = discord.Embed()
    embed.title = "Invite link"
    embed.add_field(
        name="Invite this bot for the bot",
        value="[invite](http://bit.ly/takipsizadbot1)",
    )
    await ctx.reply(embed=embed)


@bot.command()
async def http(ctx, arg1):
    imageURL = f"https://http.cat/{arg1}"
    embed = discord.Embed()
    embed.set_image(url=imageURL)
    await ctx.reply(embed=embed)


@bot.command()
async def robloxad(ctx):
    urls = [
        "https://www.roblox.com/user-sponsorship/1",
        "https://www.roblox.com/user-sponsorship/2",
        "https://www.roblox.com/user-sponsorship/3",
    ]
    url = random.choice(urls)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"User-agent": "Mozilla/5.0"}) as robloxadsss:
            robloxadss = await robloxadsss.read()
            soup = BeautifulSoup(robloxadss, features="html.parser")
            embed = discord.Embed()
            embed.set_image(url=soup.find("img")["src"])
            await ctx.reply(embed=embed)


@bot.command()
async def ytinfo(ctx, arg1):
    try:
        yt = YouTube(arg1)
        await ctx.reply(
        f"""```link {arg1} \ntitle: {yt.title}
        \nauthor: {yt.author} \ndescription:\n {yt.description} \nmetadata: 
        {yt.metadata} \npublish date: {yt.publish_date} \nrating: {yt.rating} \nviews: {yt.views}```""")
    except:
        await ctx.reply("error  make sure to enter valid link")


@bot.command()
async def facepalm(ctx):
    await ctx.reply(embed=await reddit.reddit("facepalm"))


@bot.command()
async def madlads(ctx):
    await ctx.reply(embed=await reddit.reddit("madlads"))


@bot.command()
async def softwaregore(ctx):
    await ctx.reply(embed=await reddit.reddit("softwaregore"))


@bot.command(name="reddit")
async def reddt(ctx, arg1):
    user_voted = await dble.get_user_vote(user_id=ctx.author.id)
    is_premium_user = await premium.find_one({str(ctx.author.id): "true"})
    if user_voted == True or is_premium_user is not None:
        await ctx.reply(embed=await reddit.reddit(arg1))
    else:
        await ctx.reply("You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote")


@bot.command(aliases=["meme"])
async def memes(ctx):
    memesubreddit = [
        "dankmemes",
        "memes",
        "HistoryMemes",
        "PrequelMemes",
        "wholesomememes",
        "ProgrammerHumor",
        "codingmemes",
        "SkidsBeingSkids",
        "IT_Memes",
        "programmerjoke",
        "masterhacker",
    ]
    await ctx.reply(embed=await reddit.randomreddit(memesubreddit))


@bot.command(name="all")
async def lal(ctx):
    await ctx.reply(embed=await reddit.reddit("random"))


@bot.command()
async def programmerhumor(ctx):
    await ctx.reply(embed=await reddit.reddit("programmerhumor"))


@bot.command()
async def donate(ctx):
    embed = discord.Embed(title="Donate", color=0x209F69)
    embed.add_field(
        name="donate ethereum", value="0xf667485f542185d2c27B897E660a589a37b21FCc"
    )
    embed.add_field(
        name="donate bitcoin", value="bc1q4us2ueuayl4j36ju708xzez7vdpurpw33n8amv"
    )
    embed.add_field(
        name="donate bitcoin (backup)",
        value="bc1qfyzu4xcjg5tq4fmp3tfrqsnv82368w4xvwxvy2",
    )
    embed.add_field(
        name="donate dogecoin",
        value="DBBqyi3BuonKbTNJtnQzBfTB92WgK1iZZw",
    )
    embed.set_footer(text="thanks for using my bot ❤️  ")
    await ctx.reply(embed=embed)


@bot.group()
async def eth(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.reply("Invalid ethereum command passed...")





@bot.command()
async def web3version(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            ("https://ethapi.takipsizad.repl.co/api/v1/version")) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["web3version"]
            await ctx.reply(f"web3 js version : {parsed_json2}")


@eth.command()
async def balance(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f"https://ethapi.takipsizad.repl.co/api/v1/checkbal?wallet={arg1}")) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["balance"]
            await ctx.reply(f"ethereum balance: {parsed_json2}")


@eth.command()
async def ibantoadress(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f"https://ethapi.takipsizad.repl.co/api/v1/ibantoadress?Iban={arg1}")) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["adress"]
            await ctx.reply(f"adress: {parsed_json2}")


@eth.command()
async def adresstoiban(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f"https://ethapi.takipsizad.repl.co/api/v1/adresstoiban?adress={arg1}")) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["iban"]
            await ctx.reply(f"Iban: {parsed_json2}")


@eth.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def createaccount(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://ethapi.takipsizad.repl.co/api/v1/createacc",headers={"User-agent": "Mozilla/5.0"},) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json["acc"]
            parsed_json3 = parsed_json2["address"]
            parsed_json4 = parsed_json2["privateKey"]
            await ctx.author.send(
                "adress:`{0}` \n private key  **dont share with anyone** `{1}`".format(
                    parsed_json3, parsed_json4
                )
            )
            await ctx.reply(" i send it from dms")


@eth.command()
async def prices(ctx):
    prices = cg.get_price(ids="ethereum", vs_currencies="usd")
    p2 = prices["ethereum"]
    e = p2["usd"]
    await ctx.reply(f"ethereum price: {e} in usd")


@bot.listen("on_command_error")
async def on_command_error(ctx, error):
    # Unwrapping the error cause because of how discord.py raises some of them
    error = error.__cause__ or error
    errors = []
    errors.append(error)
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(
            f"That command is on cooldown for `{error.retry_after:,.0f}` more seconds!"
        )
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.reply("make sure to enter a required argument")

    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.reply("some error happened give me enough permissions for that ")
    if isinstance(error, commands.NotOwner):
        await ctx.reply("you are not my owner ")


@bot.listen("on_slash_command_error")
async def on_slash_command_error(ctx, error):
    # Unwrapping the error cause because of how discord.py raises some of them
    error = error.__cause__ or error
    errors = []
    errors.append(error)
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(
            f"That command is on cooldown for `{error.retry_after:,.0f}` more seconds!"
        )
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.reply("make sure to enter a required argument")

    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.reply("some error happened give me enough permissions for that ")
    if isinstance(error, commands.NotOwner):
        await ctx.reply("you are not my owner ")


@bot.command()
async def cryptoprices(ctx, arg1, arg2):
    prices = cg.get_price(ids=arg1, vs_currencies=arg2)
    p2 = prices[arg1]
    e = p2[arg2]
    embed = discord.Embed()
    embed.add_field(name=f"{arg1} prices",value=f"{arg1} price: {e} in {arg2}")
    await ctx.reply(f"{arg1} price: {e} in {arg2}")


@bot.event
async def on_message(message):
    channel = bot.get_channel(811654102723330068)
    if message.guild.id == 827066784896253961:
        await channel.send(message.content)
        asyncio.sleep(1)
        await channel.send(message.author)
    await bot.process_commands(message)



@bot.listen("on_command")
async def on_command(ctx):
    channel = bot.get_channel(805355006551130122)
    embed = discord.Embed()
    embed.set_author(name="Command invoked")
    embed.add_field(name="Command", value=f"``{ctx.command}``")
    embed.add_field(name="Author", value=f"``{ctx.author}``")
    embed.add_field(name="Author ID", value=f"``{ctx.author.id}``")
    embed.add_field(name="Channel", value=f"``{ctx.channel}``")
    embed.add_field(name="Channel ID", value=f"``{ctx.channel.id}``")
    embed.add_field(name="Guild", value=f"``{ctx.guild}``")
    embed.add_field(name="Guild ID", value=f"``{ctx.guild.id}``")
    await channel.send(embed=embed)


@bot.listen("on_slash_command")
async def on_commsand(ctx):
    channel = bot.get_channel(805355006551130122)
    embed = discord.Embed()
    embed.set_author(name="Slash Command invoked")
    embed.add_field(name="Command", value=f"``{ctx.command}``")
    embed.add_field(name="Author", value=f"``{ctx.author}``")
    embed.add_field(name="Author ID", value=f"``{ctx.author.id}``")
    embed.add_field(name="Channel", value=f"``{ctx.channel}``")
    embed.add_field(name="Channel ID", value=f"``{ctx.channel.id}``")
    embed.add_field(name="Guild", value=f"``{ctx.guild}``")
    embed.add_field(name="Guild ID", value=f"``{ctx.guild.id}``")
    await channel.send(embed=embed)


@bot.command()
async def catfact(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://cat-fact.herokuapp.com/facts/random",headers={"User-agent": "Mozilla/5.0"},) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json["text"]
            await ctx.reply(f"random cat fact {parsed_json2}")


@bot.command()
async def generatecode(ctx):
    if ctx.author.id == 542380989775740929:
        prmcodess = str(uuid.uuid4())
        prmdata = {prmcodess: "pff"}
        await prmc.insert_one(prmdata)
        await ctx.author.send(f"{prmcodess} generated code")
    else:
        raise commands.NotOwner("")


@bot.command()
async def usecode(ctx, arg1):
    xx = {f"{arg1}": "pff"}
    x = await prmc.find_one(xx)
    if not None is x:
        await prmc.delete_one({str(arg1): "pff"})
        await premium.insert_one({str(ctx.author.id): "true"})
    else:
        await ctx.reply("Invalid code")

@slash.slash(name="info", description="Info command")
async def _info(ctx):
    await ctx.respond()
    await ctx.send(
        f"""
discord py version {discord.__version__}
aiohttp version  {aiohttp.__version__}
discord slash version  {discord_slash.__version__}
motor (mongodb) version  {motor.version}
os version {platform.platform(aliased=0, terse=0)}
python info {platform.python_implementation()} {platform.python_version()}
on {len(bot.guilds)} guilds 
made by takipsizad#1919"""
    )


@slash.slash(name="reddit", description="Reddit command")
async def _redd_t(ctx, subreddit):
    user_voted = await dble.get_user_vote(user_id=ctx.author.id)
    is_premium_user = await premium.find_one({str(ctx.author.id): "true"})
    if user_voted == True or is_premium_user is not None:
        await ctx.reply(embed=await reddit.reddit(subreddit))
    else:
        await ctx.reply("You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote")




@slash.slash(name="donate", description="Donate command")
async def __donate(ctx):
    embed = discord.Embed(title="Donate", color=0x209F69)
    embed.add_field(
        name="donate ethereum", value="0xf667485f542185d2c27B897E660a589a37b21FCc"
    )
    embed.add_field(
        name="donate bitcoin", value="bc1q4us2ueuayl4j36ju708xzez7vdpurpw33n8amv"
    )
    embed.add_field(
        name="donate bitcoin (backup)",
        value="bc1qfyzu4xcjg5tq4fmp3tfrqsnv82368w4xvwxvy2",
    )
    embed.set_footer(text="thanks for using my bot ❤️  ")
    await ctx.send(embed=embed)


@slash.slash(name="cryptoprices", description="cryptoprice command")
async def __cryptoprices(ctx, cryptocurrency, currency):
    prices = cg.get_price(ids=cryptocurrency, vs_currencies=currency)
    p2 = prices[cryptocurrency]
    e = p2[currency]
    await ctx.send(f"{cryptocurrency} price: {e} in {currency}")


@slash.slash(name="support", description="Support command")
async def __support(ctx):
    embed = discord.Embed()
    embed.title = "Invite link"
    embed.add_field(
        name="Support server",
        value="[support](https://discord.gg/4uW3mTxx5S)",
    )
    await ctx.send(embed=embed)


app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"
Thread(target=app.run,args=("0.0.0.0",8080)).start()
bot.loop.create_task(ch_pr())
bot.run(token)
