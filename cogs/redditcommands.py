import discord
import os
import topgg
from datetime import datetime
from discord.ext import commands
from utils import reddit
import asyncio
import motor
import discord_slash.cog_ext
from discord_slash import cog_ext
loop = asyncio.get_event_loop()

dbltoken = os.getenv("dbltoken")

class Redditcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dbl = topgg.DBLClient(bot=self.bot, token=dbltoken,loop=loop)
        dburl = os.getenv("db")
        self.client = motor.motor_tornado.MotorClient(dburl)
        db = self.client["db"]
        self.premium = db.premium
        self.subredditdb = db.memessubreddits

    @commands.command()
    async def facepalm(self,ctx):
        await ctx.reply(embed=await reddit.reddit("facepalm"))

    @commands.command()
    async def madlads(self,ctx):
        await ctx.reply(embed=await reddit.reddit("madlads"))
    
    @commands.command()
    async def softwaregore(self, ctx):
        await ctx.reply(embed=await reddit.reddit("softwaregore"))
    
    @commands.group(name="reddit")
    async def reddt(self, ctx, subreddit):
        user_voted = True #await self.dbl.get_user_vote(user_id=ctx.author.id)
        is_premium_user = await self.premium.find_one({str(ctx.author.id): "true"})
        if user_voted == True or is_premium_user is not None:
            await ctx.reply(embed=await reddit.reddit(subreddit))
        else:
            await ctx.reply(
                "You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote"
            )

    @commands.group(name="memes", aliases=["meme"])
    async def memes(self, ctx):
        if ctx.invoked_subcommand is None:
            subredditdb = self.subredditdb
            memesubreddits = await subredditdb.find_one({"userId": f"{ctx.author.id}"})
            if not memesubreddits:
                await ctx.reply("make sure to add meme subreddits with ta!!memes add")
            else:
                memesubreddit = memesubreddits["subreddits"].split(",")
                memesubreddit = memesubreddit.replace(" ","")
                print(memesubreddit)
                await ctx.reply(embed=await reddit.randomreddit(memesubreddit))

    @memes.command()
    async def add(self, ctx,*,args):
        user_voted = True #await self.dbl.get_user_vote(user_id=ctx.author.id)
        is_premium_user = await self.premium.find_one({str(ctx.author.id): "true"})
        if user_voted == True or is_premium_user is not None:
            data = {"userId": f"{ctx.author.id}","subreddits": f"{args}"}
            datatofind = {"userId": f"{ctx.author.id}"}
            subredditdb = self.subredditdb
            userdata = await subredditdb.find_one(datatofind)
            if userdata is not  None:
                await subredditdb.update_one(userdata, {'$set': data})
            else:
                result = await subredditdb.insert_one(data)
        await ctx.reply(
            "You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote"
        )
    @memes.command(name="list")
    async def lists(self, ctx):
        datatofind = {"userId": f"{ctx.author.id}"}
        subredditdb = self.subredditdb
        userdata = await subredditdb.find_one(datatofind)
        await ctx.reply(f"chosen subreddits:{userdata['subreddits']}")

    @commands.command(name="all")
    async def lal(self, ctx):
        await ctx.reply(embed=await reddit.reddit("random"))

    @commands.command()
    async def programmerhumor(self, ctx):
        await ctx.reply(embed=await reddit.reddit("programmerhumor"))
    
    @cog_ext.cog_slash(name="reddit", description="Reddit command")
    async def _redd_t(self, ctx, subreddit: str):
        user_voted = True #await self.dbl.get_user_vote(user_id=ctx.author.id)
        is_premium_user = await self.premium.find_one({str(ctx.author.id): "true"})
        if user_voted == True or is_premium_user is not None:
            await ctx.send(embed=await reddit.reddit(subreddit)) 
        else:
            await ctx.send(
                "You must vote for the bot vote link: https://top.gg/bot/555036314077233172/vote"
            )  # pain

def setup(bot):
    bot.add_cog(Redditcommands(bot))
