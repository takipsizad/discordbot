import discord
import motor
import os
from discord.ext import commands

class Premiumdetect(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        dburl = os.getenv("db")
        self.client = motor.motor_tornado.MotorClient(dburl)
        db = self.client["db"]
        self.prmc = db.premiumcode
        self.premium = db.premium

    @commands.command()
    async def usecode(self, ctx, arg1):
        xx = {f"{arg1}": "pff"}
        x = await self.prmc.find_one(xx)
        if not None is x:
            await self.prmc.delete_one({str(arg1): "pff"})
            await self.premium.insert_one({str(ctx.author.id): "true"})
        else:
            await ctx.reply("Invalid code")
    
    


def setup(bot):
    bot.add_cog(Premiumdetect(bot))