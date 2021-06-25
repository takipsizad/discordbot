import discord
from discord.ext import commands
from utils.fetch import fetch
import asyncio
import random
from discord.ext.commands import has_permissions
loop = asyncio.get_event_loop()


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ipcheck(self,ctx, arg1):
        async with fetch(
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
        async with fetch(
            (f"https://termsite.takipsizad.tk/api/langdetect?text={arg1}"),
            headers={"User-agent": "Mozilla/5.0"},
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["lang"]
            await ctx.reply(f"language: {parsed_json2}")

    @commands.command()
    async def serverversion(self,ctx):
        async with fetch(
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
    async def robloxad(self,ctx):
        urls = [
            "https://www.roblox.com/user-sponsorship/1",
            "https://www.roblox.com/user-sponsorship/2",
            "https://www.roblox.com/user-sponsorship/3",
        ]
        url = random.choice(urls) 
        async with fetch(url, headers={"User-agent": "Mozilla/5.0"}) as robloxadsss:
            robloxadss = await robloxadsss.read()
            soup = BeautifulSoup(robloxadss, features="html.parser")
            embed = discord.Embed()
            embed.set_image(url=soup.find("img")["src"])
            embed.add_field(
                name=f'{soup.find("a")["title"]}',
                value=f'[{soup.find("a")["title"]}]({soup.find("a")["href"]})',
            )
            await ctx.reply(embed=embed)

    @commands.command()
    async def catfact(self, ctx):
        async with fetch(
            "https://cat-fact.herokuapp.com/facts/random",
            headers={"User-agent": "Mozilla/5.0"},
        ) as res:
            parsed_json = await res.json()
            parsed_json2 = parsed_json["text"]
            await ctx.reply(f"random cat fact {parsed_json2}")

    @commands.command(aliases=["create-invite", "createinvite"])
    async def create_invite(self, ctx):
        link = await ctx.channel.create_invite()
        await ctx.reply(f"Here is an instant invite to your server: {str(link)}")


    @commands.command(aliases=["delete-invite", "delete_invite"])
    @has_permissions(manage_guild=True)
    async def deleteinvite(self, ctx, arg1):
        try:
            await bot.delete_invite(arg1)
            await ctx.reply("invite deleted")
        except:
            await ctx.reply("error deleting invite")

    @commands.command()
    async def http(ctx, arg1):
        imageURL = f"https://http.cat/{arg1}"
        embed = discord.Embed()
        embed.set_image(url=imageURL)
        await ctx.reply(embed=embed)



def setup(bot):
    bot.add_cog(Utils(bot))
