import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
from discord.ext import commands
import platform
from discord.ext.commands import has_permissions
import asyncio
import random
from bs4 import BeautifulSoup
from pytube import YouTube
import reddit
import aiohttp
from pycoingecko import CoinGeckoAPI
import jishaku
import discord_slash
import dbl
import motor
import uuid
from discord_slash import SlashCommand
from threading import Thread
from flask import Flask
cg = CoinGeckoAPI()
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
ıntents = discord.Intents.all()
bot = commands.Bot(command_prefix="ta!!",intents=ıntents)
slash = SlashCommand(bot)
token = os.getenv('token')
dbltoken = os.getenv('dbltoken')
db = os.getenv('db')
client = motor.motor_tornado.MotorClient(db)
mydb = client["db"]
prmc = mydb.premiumcode
premium = mydb.premium
bot.remove_command("help")
bot.load_extension("help")
bot.load_extension('jishaku')


dble = dbl.DBLClient(bot=bot, token=dbltoken, autopost = True)
async def ch_pr():
    while True:
        await bot.wait_until_ready()
        statuss = ["prefix : ta!!","made with python3 lol","0xf667485f542185d2c27B897E660a589a37b21FCc my ethereum adress dont forget to donate :D ",
        "made by takipsizad", f"on {len(bot.guilds)} servers","ta!!help for help" 
        , f"on {round(bot.latency * 1000)} ping" , f"discord py version: {(discord.__version__)}"
        ,"ta!!vote :D "]
        statusss = discord.Game(random.choice(statuss))
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=statusss)
        await asyncio.sleep(20)


bot.loop.create_task(ch_pr())

@bot.command()
async def ping(ctx):
     await ctx.reply(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ipcheck(ctx,arg1):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.iplegit.com/info?ip=' + str(arg1),headers ={'User-agent': 'Mozilla/5.0'}) as res:
                jsonr = json.dumps(await res.json())
                parsed_json = json.loads(jsonr)
                parsed_json2 = parsed_json['bad']
                parsed_json3 = parsed_json['type']
                parsed_json4 = parsed_json['ip']
                await ctx.reply('bad: {} type: {} ip: {}'.format(str(parsed_json2), str(parsed_json3), str(parsed_json4)))
    except:
        await ctx.reply('error make sure you write ip to check')


@bot.event
async def on_ready():
    print("Your bot is ready")

@bot.command()
async def langdetect(ctx,arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get(('https://termsite.takipsizad.repl.co/api/langdetect?text=' + arg1),headers ={'User-agent': 'Mozilla/5.0'}) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['lang']
            await ctx.reply('language: {}'.format(parsed_json2))

@bot.command()
async def serverversion(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(('https://termsite.takipsizad.repl.co/api/serverversion'),headers ={'User-agent': 'Mozilla/5.0'}) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['serverversion']
            await ctx.reply('server version {}'.format(parsed_json2))

@bot.command()
async def execute(ctx, *,args):
    if 542380989775740929 == ctx.author.id:
        output = eval(args)
        await ctx.reply(output)
    else:
        await ctx.reply('nah you arent my owner')

@bot.command()
async def info(ctx):
    await ctx.reply('discord py version {} \nos version {}\npython info {} {}\non {} guilds \nmade by takipsizad'.format(discord.__version__,platform.platform(aliased=0, terse=0),platform.python_implementation(),
    platform.python_version(),len(bot.guilds)))

@bot.event
async def on_guild_join(guild):
    await bot.wait_until_ready()
    channel = bot.get_channel(805355006551130122)
    await channel.send('i joined {}'.format(guild))

@bot.event
async def on_guild_remove(guild):
    await bot.wait_until_ready()
    channel = bot.get_channel(805355006551130122)
    await channel.send('i leaved {}'.format(guild))

@bot.command()
async def getwidget(ctx):
    await ctx.reply(await bot.fetch_widget(ctx.guild.id))

@bot.command(aliases=['create-invite', 'createinvite'])
async def create_invite(ctx):
    link = await ctx.channel.create_invite()
    await ctx.reply("Here is an instant invite to your server: " + str(link))

@bot.command(aliases=['delete-invite', 'delete_invite'])
@has_permissions(manage_guild=True)  
async def deleteinvite(ctx,arg1):
    try:
        await bot.delete_invite(arg1)
        await ctx.reply("invite deleted")
    except:
        await ctx.reply('error deleting invite')
    

@bot.command()
async def echo(ctx, *,args):
    if not '@' in args:
        await ctx.send(args)
    else:
        await ctx.reply('dont send mentions')

@bot.command()
async def vote(ctx):
    embed = discord.Embed()
    embed.title = "Vote link"
    embed.add_field(name="vote link:",value="[vote](https://top.gg/bot/555036314077233172/vote?refferer=takipsizadbot)")
    await ctx.reply(embed=embed)


@bot.command()
async def invite(ctx):
    embed = discord.Embed()
    embed.title = "Invite link"
    embed.add_field(name='Invite this bot for the bot',value='[invite](http://bit.ly/takipsizadbot1)')
    await ctx.reply(embed=embed)

@bot.command()
async def http(ctx,arg1):
    imageURL = f"https://http.cat/{arg1}"
    embed = discord.Embed()
    embed.set_image(url=imageURL)
    await ctx.reply(embed=embed)


@bot.command()
async def robloxad(ctx):
    urls = ['https://www.roblox.com/user-sponsorship/1','https://www.roblox.com/user-sponsorship/2','https://www.roblox.com/user-sponsorship/3']
    url = random.choice(urls)
    async with aiohttp.ClientSession() as session:
        async with session.get((url),headers ={'User-agent': 'Mozilla/5.0'}) as robloxadsss:
            robloxadss = await robloxadsss.text()
            soup = BeautifulSoup(robloxadss,features="html.parser")
            embed = discord.Embed()
            embed.set_image(url=soup.find('img')['src'])
            await ctx.reply(embed=embed)

@bot.command()
async def ytinfo(ctx,arg1):
    try:
        yt = YouTube(arg1)
        await ctx.reply(f"""```link {arg1} \ntitle: {yt.title}
        \nauthor: {yt.author} \ndescription:\n {yt.description} \nmetadata: 
        {yt.metadata} \npublish date: {yt.publish_date} \nrating: {yt.rating} \nviews: {yt.views}```""")
    except:
        await ctx.reply('error  make sure to enter valid link')


@bot.command()
async def facepalm(ctx):
    await ctx.reply(embed=await reddit.reddit('facepalm'))

@bot.command()
async def madlads(ctx):
    await ctx.reply(embed=await reddit.reddit('madlads'))

@bot.command()
async def softwaregore(ctx):
    await ctx.reply(embed=await reddit.reddit('softwaregore'))

@bot.command(name='reddit')
async def reddt(ctx,arg1):
    e = await dble.get_user_vote(user_id=ctx.author.id)
    prm = await premium.find_one({str(ctx.author.id):"true"})
    if e == True:
        await ctx.reply(embed=await reddit.reddit(arg1))
    elif prm == None:
        await ctx.reply("You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote")
    else:
        await ctx.reply(embed=await reddit.reddit(arg1))

@bot.command(aliases=['meme'])
async def memes(ctx):
    memesubreddit = ['dankmemes','memes','HistoryMemes','PrequelMemes','wholesomememes','ProgrammerHumor','codingmemes','SkidsBeingSkids','IT_Memes','programmerjoke','masterhacker']
    await ctx.reply(embed=await reddit.randomreddit(memesubreddit))

@bot.command(name="all")
async def lal(ctx):
    await ctx.reply(embed=await reddit.reddit('random'))
@bot.command()
async def programmerhumor(ctx):
    await ctx.reply(embed=await reddit.reddit('programmerhumor'))

@bot.command()
async def donate(ctx):
    embed=discord.Embed(title="Donate",color=0x209f69)
    embed.add_field(name='donate ethereum',value='0xf667485f542185d2c27B897E660a589a37b21FCc')
    embed.set_footer(text="thanks for using my bot ❤️  ")
    await ctx.reply(embed=embed) 

@bot.group()
async def eth(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.reply('Invalid ethereum command passed...')

@eth.command()
async def gasprice(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(('https://ethapi.takipsizad.repl.co/api/gasprices')) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['gasprices']
            await ctx.reply('ethereum gas prices: {}'.format(parsed_json2))
@bot.command()
async def web3version(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(('https://ethapi.takipsizad.repl.co/api/version')) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['web3version']
            await ctx.reply('web3 js version : {}'.format(parsed_json2))

@eth.command()
async def balance(ctx,arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f'https://ethapi.takipsizad.repl.co/api/checkbal?wallet={arg1}')) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['balance']
            await ctx.reply('ethereum balance: {}'.format(parsed_json2))

@eth.command()
async def ibantoadress(ctx,arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f'https://ethapi.takipsizad.repl.co/api/ibantoadress?Iban={arg1}')) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['adress']
            await ctx.reply('adress: {}'.format(parsed_json2))

@eth.command()
async def adresstoiban(ctx,arg1):
    async with aiohttp.ClientSession() as session:
        async with session.get((f'https://ethapi.takipsizad.repl.co/api/adresstoiban?adress={arg1}')) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['iban']
            await ctx.reply('Iban: {}'.format(parsed_json2))

@eth.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def createaccount(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://ethapi.takipsizad.repl.co/api/createacc',headers ={'User-agent': 'Mozilla/5.0'}) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['acc']
            parsed_json3 = parsed_json2['address']
            parsed_json4 = parsed_json2['privateKey']
            await ctx.author.send("adress:`{0}` \n private key  **dont share with anyone** `{1}`".format(parsed_json3,parsed_json4))
            await ctx.reply(" i send it from dms")

@eth.command()
async def prices(ctx):
    prices = cg.get_price(ids='ethereum', vs_currencies='usd')
    p2 = prices['ethereum']
    e = p2['usd']
    await ctx.reply('ethereum price: {} in usd'.format(e))

@bot.listen("on_command_error")
async def on_command_error(ctx, error):
    # Unwrapping the error cause because of how discord.py raises some of them
    error = error.__cause__ or error
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"That command is on cooldown for `{error.retry_after:,.0f}` more seconds!")
    if isinstance(error,  commands.errors.MissingRequiredArgument):
        await ctx.reply('make sure to enter a required argument')

    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.reply('some error happened give me enough permissions for that ')
    if isinstance(error, commands.NotOwner):
        await ctx.reply("you are not my owner ")

@bot.listen("on_slash_command_error")
async def on_slash_command_error(ctx, error):
    # Unwrapping the error cause because of how discord.py raises some of them
    error = error.__cause__ or error
    print(error)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"That command is on cooldown for `{error.retry_after:,.0f}` more seconds!")
    if isinstance(error,  commands.errors.MissingRequiredArgument):
        await ctx.reply('make sure to enter a required argument')

    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.reply('some error happened give me enough permissions for that ')
    if isinstance(error, commands.NotOwner):
        await ctx.reply("you are not my owner ")




@bot.command()
async def cryptoprices(ctx,arg1,arg2):
    prices = cg.get_price(ids=arg1, vs_currencies=arg2)
    p2 = prices[arg1]
    e = p2[arg2]
    await ctx.reply('{} price: {} in {}'.format(arg1,e,arg2))


@bot.event
async def on_message(message):
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
    embed.set_author(name="Command invoked")
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
        async with session.get('https://cat-fact.herokuapp.com/facts/random',headers ={'User-agent': 'Mozilla/5.0'}) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json['text']
            await ctx.reply(f"random cat fact {parsed_json2}")

@bot.command()
async def generatecode(ctx):
    if 542380989775740929 == ctx.author.id:
            prmcodess = str(uuid.uuid4())
            prmdata = {prmcodess:"pff"}
            await prmc.insert_one(prmdata)
            await ctx.author.send(f"{prmcodess} generated code")
    else:
        await ctx.reply('nah you arent my owner')

@bot.command()
async def usecode(ctx,arg1):
        xx = {f"{arg1}":"pff"}
        x = await prmc.find_one(xx)
        if not None == x:
            await prmc.delete_one({str(arg1):"pff"})
            await premium.insert_one({str(ctx.author.id):"true"})
        else:
            await ctx.reply("Invalid code")


@slash.slash(name="info",description="Info command")
async def _info(ctx):
    await ctx.respond()
    await ctx.send('discord py version {} \nos version {}\npython info {} {}\non {} guilds\nmade by takipsizad'.format(discord.__version__,platform.platform(aliased=0, terse=0),platform.python_implementation(),
    platform.python_version(),len(bot.guilds)))


@slash.slash(name="reddit",description="Reddit command")
async def _redd_t(ctx,subreddit):
    e = await dble.get_user_vote(user_id=ctx.author.id)
    prm = await premium.find_one({str(ctx.author.id):"true"})
    if e == True:
        await ctx.send(embed=await reddit.reddit(subreddit))
    elif prm == None:
        await ctx.send("You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote")
    else:
        await ctx.send(embed=await reddit.reddit(subreddit))


@slash.slash(name="donate",description="Donate command")
async def _donate(ctx):
    embed=discord.Embed(title="Donate",color=0x209f69)
    embed.add_field(name='donate ethereum',value='0xf667485f542185d2c27B897E660a589a37b21FCc')
    embed.set_footer(text="thanks for using my bot ❤️  ")
    await ctx.send(embed=embed) 


@slash.slash(name="cryptoprices",description="cryptoprice command")
async def _cryptoprices(ctx,cryptocurrency,currency):
    prices = cg.get_price(ids=cryptocurrency, vs_currencies=currency)
    p2 = prices[cryptocurrency]
    e = p2[currency]
    await ctx.send('{} price: {} in {}'.format(cryptocurrency,e,currency))

@slash.slash(name="invite",description="Invite command")
async def _invite(ctx):
    embed = discord.Embed()
    embed.title = "Invite link"
    embed.add_field(name='Invite this bot for the bot',value='[invite](http://bit.ly/takipsizadbot1)')
    await ctx.send(embed=embed)


app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

Thread(target=app.run,args=("0.0.0.0",8080)).start()

bot.run(token)