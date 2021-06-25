import discord
from discord.ext import commands
from utils.http import sessions
import asyncio
import json
loop = asyncio.get_event_loop()
session = loop.run_until_complete(sessions())

class Web3commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group()
    async def eth(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("Invalid ethereum command passed...")


    @commands.command()
    async def web3version(self, ctx):
        async with session.get(("https://ethapi.takipsizad.tk/api/v1/version")) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["web3version"]
            await ctx.reply(f"web3 js version : {parsed_json2}")


    @eth.command()
    async def gasprices(self, ctx):
        async with session.get((f"https://ethapi.takipsizad.tk/api/v1/gasprices")) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["gasprices"]
            await self, ctx.reply(f"ethereum balance: {parsed_json2} ***in wei***")


    @eth.command()
    async def balance(self, ctx, arg1):
        async with session.get(
            (f"https://ethapi.takipsizad.tk/api/v1/checkbal?wallet={arg1}")
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["balance"]
            await ctx.reply(f"ethereum gas prices: {parsed_json2} ***in wei***")


    @eth.command()
    async def ibantoadress(self, ctx, arg1):
        async with session.get(
            (f"https://ethapi.takipsizad.tk/api/v1/ibantoadress?Iban={arg1}")
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["adress"]
            await ctx.reply(f"adress: {parsed_json2}")


    @eth.command()
    async def adresstoiban(self, ctx, arg1):
        async with session.get(
            (f"https://ethapi.takipsizad.tk/api/v1/adresstoiban?adress={arg1}")
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["iban"]
            await ctx.reply(f"Iban: {parsed_json2}")


    @eth.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def createaccount(self, ctx):
        async with session.get(
            "https://ethapi.takipsizad.tk/api/v1/createacc",
            headers={"User-agent": "Mozilla/5.0"},
        ) as res:
            jsonr = json.dumps(await res.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json["acc"]
            parsed_json3 = parsed_json2["address"]
            parsed_json4 = parsed_json2["privateKey"]
            await self, ctx.author.send(
                "adress:`{0}` \n private key  **dont share with anyone** `{1}`".format(
                    parsed_json3, parsed_json4
                )
            )
            await ctx.reply("i send it from dms")


def setup(bot):
    bot.add_cog(Web3commands(bot))