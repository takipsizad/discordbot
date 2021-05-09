from discord.ext import commands
from dpymenus import Page, PaginatedMenu
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands
import discord
import motor
import os
db = os.getenv("db")
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
client = motor.motor_tornado.MotorClient(db)
mydb = client["db"]
tos = mydb.tosaccept
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context):
        page1 = Page(title='commands:', description='First page')
        page1.add_field(name='bot related commands', value="""ta!!ping
        ta!!info
        ta!!vote
        ta!!invite
        ta!!donate""")

        page2 = Page(title='commands:', description='Second page')
        page2.add_field(name='utility commands:', value="""
        ta!!ipcheck <ip>
        ta!!langdetect <string>
        ta!!serverversion
        ta!!http <http code>
        ta!!ytinfo <youtube link >
        ta!!create-invite
        ta!!delete-invite <invite>
        ta!!getwidget
        ta!!catfact
        """)

        page3 = Page(title='commands:', description='Third page')
        page3.add_field(name='reddit commands:', value="""
        ta!!programmerhumor
        ta!!softwaregore
        ta!!mcmemes
        ta!!madlads
        ta!!meme
        ta!!all
        ta!!facepalm
        ta!!reddit <subreddit>
        """)
        page4 = Page(title='commands:', description='Fourth page')
        page4.add_field(name='fun commands:', value="""ta!!robloxad
        ta!!meme""")

        page5 = Page(title='commands:', description='Fifth page')
        page5.add_field(name='ethereum commands:', value="""
        ta!!eth balance <ethereum adress>
        ta!!eth createaccount
        ta!!eth adresstoiban <ethereum adress>
        ta!!eth ibantoadress <iban>
        ta!!eth gasprices
        """)
        page6 = Page(title='commands:', description='Fifth page')
        page6.add_field(name='crypto commands:', value="""
        ta!!web3version
        ta!!cryptoprices <crypto name> <currency>
        """)
        menu = PaginatedMenu(ctx)
        menu.show_page_numbers()
        menu.set_timeout(30)
        menu.persist_on_close()
        menu.allow_multisession()
        menu.add_pages([page1, page2, page3,page4,page5,page6])
        xx = {f"{ctx.author.id}":"true"}
        x = await tos.find_one(xx)
        if  x is not None:
            await menu.open()
        else:
            embed = discord.Embed()
            embed.title = "Verify"
            embed.add_field(name="by using my bot you agree rules",value="[rules](https://gist.github.com/takipsizad/4a2755e12c31a9495c417370b956f363)")
            embed.add_field(name="Dont forget to donate for my bot",value="my ethereum adress 0xf667485f542185d2c27B897E660a589a37b21FCc")
            embed.set_footer(text="Thanks for using my bot ❤")
            await ctx.reply(embed=embed)
            await tos.insert_one({str(ctx.author.id):"true"})


def setup(bot):
    bot.add_cog(help(bot))
