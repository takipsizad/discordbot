import discord
import os
import topgg
from datetime import datetime
from discord.ext import commands
from utils import reddit
dbltoken = os.getenv("dbltoken")

class Redditcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dbl = topgg.DBLClient(bot=self.bot, token=dbltoken)

    @commands.command()
    async def facepalm(self,ctx):
        await ctx.reply(embed=await reddit.reddit("facepalm"))

    @commands.command()
    async def madlads(self,ctx):
        await ctx.reply(embed=await reddit.reddit("madlads"))
    
    @commands.command()
    async def softwaregore(self,ctx):
        await ctx.reply(embed=await reddit.reddit("softwaregore"))
    
    @commands.command(name="reddit")
    async def reddt(self, ctx, arg1):
        user_voted = await self.dbl.get_user_vote(user_id=ctx.author.id)
        is_premium_user = await premium.find_one({str(ctx.author.id): "true"})
        if user_voted == True or is_premium_user is not None:
            await ctx.reply(embed=await reddit.reddit(arg1))
        else:
            await ctx.reply(
                "You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote"
            )

    @commands.command(aliases=["meme"])
    async def memes(self,ctx):
        memesubreddit = [
            "dankmemes",
            "memes",
            "HistoryMemes",
            "PrequelMemes",
            "wholesomememes",
            "ProgrammerHumor",
            "codingmemes",
            "SkidsBeingSkids",
            "IT_Memes",
            "programmerjoke",
            "masterhacker",
        ]
        await ctx.reply(embed=await reddit.randomreddit(memesubreddit))

    @commands.command(name="all")
    async def lal(ctx):
        await ctx.reply(embed=await reddit.reddit("random"))

    @commands.command()
    async def programmerhumor(ctx):
        await ctx.reply(embed=await reddit.reddit("programmerhumor"))

def setup(bot):
    bot.add_cog(Redditcommands(bot))