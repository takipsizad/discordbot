import discord
from discord.ext import commands


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


def setup(bot):
    bot.add_cog(Botcmds(bot))