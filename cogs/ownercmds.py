import discord
from discord.ext import commands


class Owner_commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def execute(self,ctx,* , args):
        if ctx.author.id == 542380989775740929:
            args = str(args)
            print(args)
            output = eval(args)
            await ctx.reply(output)
        else:
            raise commands.NotOwner("")


def setup(bot):
    bot.add_cog(Owner_commands(bot))