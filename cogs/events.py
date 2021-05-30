import discord
from discord.ext import commands
import topgg


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send(f"i joined {guild}")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send("ready")
        print("Bot is ready")

    @commands.Cog.listener()
    async def on_connect(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send("connecting")

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send(f"i leaved {guild}")


def setup(bot):
    bot.add_cog(Events(bot))