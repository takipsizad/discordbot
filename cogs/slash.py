import discord
from discord.ext import commands
import discord_slash.cog_ext
from discord_slash import cog_ext
from motor import version as mtr_version
from aiohttp import __version__ as aiohttp_ver
import discord_slash
import platform
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @cog_ext.cog_slash(name="info", description="Info command")
    async def _info(self, ctx,):
        await ctx.send(
            f"""
discord py version {discord.__version__}
aiohttp version  {aiohttp_ver}
discord slash version  {discord_slash.__version__}
motor (mongodb) version  {mtr_version}
os version {platform.platform(aliased=0, terse=0)}
python info {platform.python_implementation()} {platform.python_version()}
on {len(self.bot.guilds)} guilds
made by takipsizad#1919 / takipsizad#9999""")  #





    @cog_ext.cog_slash(name="donate", description="Donate command")
    async def __donate(self, ctx):
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
        embed.set_footer(text="thanks for using my bot ❤️  ")
        await ctx.send(embed=embed)


    @cog_ext.cog_slash(name="cryptoprices", description="cryptoprice command")
    async def __cryptoprices(self, ctx, cryptocurrency: str, currency: str):
        prices = cg.get_price(ids=cryptocurrency, vs_currencies=currency)
        p2 = prices[cryptocurrency]
        e = p2[currency]
        await ctx.send(f"{cryptocurrency} price: {e} in {currency}")


    @cog_ext.cog_slash(name="support", description="Support command")
    async def __support(self, ctx):
        embed = discord.Embed()
        embed.title = "Invite link"
        embed.add_field(
            name="Support server",
            value="[support](https://discord.gg/4uW3mTxx5S)",
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Slash(bot))