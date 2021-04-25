#from RestrictedPython import compile_restricted
#
#from RestrictedPython import __builtins__
#from RestrictedPython import limited_builtins
#from RestrictedPython import utility_builtins
#import discord
#from discord.ext import commands
#
#
#
#
#
#class safeeval(commands.Cog):
#    def __init__(self, bot):
#        self.bot=bot
#
#
#    @commands.command()
#    async def eval(self,ctx, *, args):
#        source_code = f"""def function(args):
#            token = "nosneak"
#            bot = "nosneak"
#            ctx = "nosneak"
#            return {args}
#        """
#
#
#
#        try:
#            byte_code = compile_restricted(
#                source_code,
#                filename='<inline code>',
#                mode='exec'
#            )
#            loc = {}
#            __builtins__['args']=args
#            exec(byte_code, {'__builtins__': __builtins__}, loc)
#            await ctx.send(loc['function'](args))
#        except Exception as e:
#            await ctx.send(e)
#
#
#def setup(bot):
#    bot.add_cog(safeeval(bot))