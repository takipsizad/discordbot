import discord
from discord.ext import commands
from utils.fetch import fetch
import asyncio
import random
from bs4 import BeautifulSoup
from discord.ext.commands import has_permissions
from pytube import YouTube
from pycoingecko import CoinGeckoAPI
from utils.proxy import randomproxy
cg = CoinGeckoAPI()
loop = asyncio.get_event_loop()


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ipcheck(self,ctx, arg1):
        res = await  fetch(
            f"https://api.iplegit.com/info?ip={str(arg1)}",
            headers={"User-agent": "Mozilla/5.0"},
        )
        parsed_json = await res.json()
        parsed_json2 = parsed_json["bad"]
        parsed_json3 = parsed_json["type"]
        parsed_json4 = parsed_json["ip"]
        await ctx.reply(
            f"bad: { str(parsed_json2)} type: {str(parsed_json3)} ip: {str(parsed_json4)}"
        )

    @commands.command()
    async def langdetect(self,ctx, arg1):
        res = await fetch(
            (f"https://termsite.takipsizad.repl.co/api/langdetect?text={arg1}"),
            headers={"User-agent": "Mozilla/5.0"},
        )
        parsed_json = await res.json()
        parsed_json2 = parsed_json["lang"]
        await ctx.reply(f"language: {parsed_json2}")

    @commands.command()
    async def serverversion(self,ctx):
        res = await fetch(
            ("https://termsite.takipsizad.repl.co/api/serverversion"),
            headers={"User-agent": "Mozilla/5.0"},
        )
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
        robloxadsss = await fetch(url, headers={"User-agent": "Mozilla/5.0"})
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
        res = await fetch(
            "https://cat-fact.herokuapp.com/facts/random",
            headers={"User-agent": "Mozilla/5.0"})
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
            await self.bot.delete_invite(arg1)
            await ctx.reply("invite deleted")
        except:
            await ctx.reply("error deleting invite")

    @commands.command()
    async def http(self , ctx, arg1):
        imageURL = f"https://http.cat/{arg1}"
        embed = discord.Embed()
        embed.set_image(url=imageURL)
        await ctx.reply(embed=embed)

    @commands.command() # pytube wont working
    async def ytinfo(self , ctx, arg1: str):
        try:
            yt = YouTube(f"{arg1}")
            await ctx.reply(
                f"""```link {arg1} \ntitle: {yt.title}
            \nauthor: {yt.author} \ndescription:\n {yt.description} \nmetadata: 
            {yt.metadata} \npublish date: {yt.publish_date} \nrating: {yt.rating} \nviews: {yt.views}```"""
            )
        except:
            await ctx.reply("error  make sure to enter valid link")
    
    @commands.command()
    async def cryptoprices(self, ctx, arg1, arg2):
        prices = cg.get_price(ids=arg1, vs_currencies=arg2)
        p2 = prices[arg1]
        e = p2[arg2]
        embed = discord.Embed()
        embed.add_field(name=f"{arg1} prices", value=f"{arg1} price: {e} in {arg2}")
        await ctx.reply(f"{arg1} price: {e} in {arg2}")
    
    @commands.command()
    async def randomproxy(self, ctx):
        await ctx.reply(await randomproxy())
    @commands.command()
    async def guvenlinet(self,ctx,argument1):
        response = await fetch("https://guvenlinet.org.tr/ajax/sorgu/sorgula.php",method="POST", headers={"User-agent": "Mozilla/5.0"},
        data={"domain_name": argument1 ,"security_code":"wwwwww"} )
        soup = BeautifulSoup(await response.text(),features="html5lib")
        e = soup.find_all(id="profile")
        list2 = []
        for element in e:
            elements = BeautifulSoup(str(element),features="html5lib").find_all("img")
            for elem in elements:
                if str(elem) != "[]":
                    list2.append(elem.get("src"))
        if list2[0] == "/s/images/error.png":
            await ctx.reply("blocked in all family profiles")
        elif list2[1] == "/s/images/error.png":
            await ctx.reply("blocked in child profile")
        elif list2[1] == "/s/images/success.png":
            await ctx.reply(f"{argument1} is not blocked")
        elif list2[1] == "/s/images/warning.png":
            await ctx.reply("warning (not checked) ( can not be accessed in child profile")

    @commands.command()
    async def fuel_price(self,ctx,arg):
        res = await fetch(f"https://api.opet.com.tr/api/fuelprices/prices?ProvinceCode={arg}&IncludeAllProducts=true", headers={"User-agent": "Mozilla/5.0"})
        parsed_json = await res.json()
        parsed_json2 = parsed_json[0]["prices"]
        await ctx.reply(f"fuel prices {parsed_json2}")


async def setup(bot):
    await bot.add_cog(Utils(bot))
