import discord
from discord.ext import commands


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot=bot



def setup(bot):
    bot.add_cog(Slash(bot))