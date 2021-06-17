import discord
from discord.ext import commands


class Premiumdetect(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def usecode(ctx, arg1):
        xx = {f"{arg1}": "pff"}
        x = await prmc.find_one(xx)
        if not None is x:
            await prmc.delete_one({str(arg1): "pff"})
            await premium.insert_one({str(ctx.author.id): "true"})
        else:
            await ctx.reply("Invalid code")


def setup(bot):
    bot.add_cog(Premiumdetect(bot))