import discord
from discord.ext import commands
import uuid


class Owner_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def execute(self, ctx, *, args):
        if ctx.author.id == 542380989775740929:
            args = str(args)
            print(args)
            output = eval(args)
            await ctx.reply(output)
        else:
            raise commands.NotOwner("")

    @commands.command()
    async def generatecode(ctx):
        if ctx.author.id == 542380989775740929:
            prmcodess = str(uuid.uuid4())
            prmdata = {prmcodess: "pff"}
            await prmc.insert_one(prmdata)
            await ctx.author.send(f"{prmcodess} generated code")
        else:
            raise commands.NotOwner("")
    
    @commands.command()
    async def devinfo(ctx):
        if ctx.author.id == 542380989775740929:
            mem = psutil.virtual_memory()
            await ctx.reply(f"""{mem}""")
        else:
            raise commands.NotOwner("")


def setup(bot):
    bot.add_cog(Owner_commands(bot))
