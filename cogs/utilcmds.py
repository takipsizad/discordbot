import discord
from discord.ext import commands
from utils.http import sessions
import asyncio
loop = asyncio.get_event_loop()
session = loop.run_until_complete(sessions())


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ipcheck(self,ctx, arg1):
        async with session.get(
            f"https://api.iplegit.com/info?ip={str(arg1)}",
            headers={"User-agent": "Mozilla/5.0"},
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["bad"]
            parsed_json3 = parsed_json["type"]
            parsed_json4 = parsed_json["ip"]
            await ctx.reply(
                f"bad: { str(parsed_json2)} type: {str(parsed_json3)} ip: {str(parsed_json4)}"
            )

    @commands.command()
    async def langdetect(self,ctx, arg1):
        async with session.get(
            (f"https://termsite.takipsizad.tk/api/langdetect?text={arg1}"),
            headers={"User-agent": "Mozilla/5.0"},
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["lang"]
            await ctx.reply(f"language: {parsed_json2}")

    @commands.command()
    async def serverversion(self,ctx):
        async with session.get(
            ("https://termsite.takipsizad.tk/api/serverversion"),
            headers={"User-agent": "Mozilla/5.0"},
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["serverversion"]
            await ctx.reply(f"server version {parsed_json2}")
        

    @commands.command()
    async def getwidget(self, ctx):
        await ctx.reply(await self.bot.fetch_widget(ctx.guild.id))
    
    @commands.command()
    async def robloxad(ctx):
        urls = [
            "https://www.roblox.com/user-sponsorship/1",
            "https://www.roblox.com/user-sponsorship/2",
            "https://www.roblox.com/user-sponsorship/3",
        ]
        url = random.choice(urls)
        async with session.get(url, headers={"User-agent": "Mozilla/5.0"}) as robloxadsss:
            robloxadss = await robloxadsss.read()
            soup = BeautifulSoup(robloxadss, features="html.parser")
            embed = discord.Embed()
            embed.set_image(url=soup.find("img")["src"])
            embed.add_field(
                name=f'{soup.find("a")["title"]}',
                value=f'[{soup.find("a")["title"]}]({soup.find("a")["href"]})',
            )
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Utils(bot))
