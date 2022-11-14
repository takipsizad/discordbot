import discord
from discord.ext import commands
import uuid
import os
import motor
import psutil


class Owner_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        dburl = os.getenv("db")
        self.client = motor.motor_tornado.MotorClient(dburl)
        db = self.client["db"]
        self.prmc = db.premiumcode
        self.premium = db.premium

    @commands.command()
    async def execute(self, ctx, *, args):
        if ctx.author.id == 849518771268878426:
            args = str(args)
            print(args)
            output = eval(args)
            await ctx.reply(output)
        else:
            raise commands.NotOwner("")

    @commands.command()
    async def generatecode(self,ctx):
        if ctx.author.id == 849518771268878426:
            prmcodess = str(uuid.uuid4())
            prmdata = {prmcodess: "pff"}
            await self.prmc.insert_one(prmdata)
            await ctx.author.send(f"{prmcodess} generated code")
        else:
            raise commands.NotOwner("")

    @commands.command()
    async def devinfo(self,ctx):
        if ctx.author.id == 849518771268878426:
            mem = psutil.virtual_memory()
            await ctx.reply(f"""{mem}""")
        else:
            raise commands.NotOwner("")

async def setup(bot):
    await bot.add_cog(Owner_commands(bot))
