import discord
from discord.ext import commands
import platform
from motor import version as mtr_version
from aiohttp import __version__ as aiohttp_ver
class Botcmds(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def donate(self,ctx):
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

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong! In {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def echo(self, ctx, *, args):
        if not "@" in args:
            await ctx.send(args)
        else:
            await ctx.reply("dont send mentions")

    @commands.command()
    async def info(self, ctx):
        await ctx.reply(
            f"""
    discord py version {discord.__version__}
    aiohttp version  {aiohttp_ver}
    discord slash version  {discord_slash.__version__}
    motor (mongodb) version  {mtr_version}
    os version {platform.platform(aliased=0, terse=0)}
    python info {platform.python_implementation()} {platform.python_version()}
    on {len(self.bot.guilds)} guilds
    made by takipsizad#1919 / takipsizad#9999""")  # aaaaaaaaaaaaaaaaaaaaa


def setup(bot):
    bot.add_cog(Botcmds(bot))