import discord
from discord.ext import commands
import dbl


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send(f"i joined {guild}")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send("ready")
        print("Bot is ready")

    @commands.Cog.listener()
    async def on_connect(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send("connecting")
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(805355006551130122)
        await channel.send(f"i leaved {guild}")

    @commands.Cog.listener("on_command_error")
    async def on_command_error(self, ctx, error):
        # Unwrapping the error cause because of how discord.py raises some of them
        error = error.__cause__ or error
        errors = []
        errors.append(error)
        print(error)
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(
                f"That command is on cooldown for `{error.retry_after:,.0f}` more seconds!"
            )
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.reply("make sure to enter a required argument")

        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.reply("some error happened give me enough permissions for that ")
        if isinstance(error, commands.NotOwner):
            await ctx.reply("you are not my owner ")


    @commands.Cog.listener("on_slash_command_error")
    async def on_slash_command_error(self, ctx, error):
        # Unwrapping the error cause because of how discord.py raises some of them
        error = error.__cause__ or error
        errors = []
        errors.append(error)
        print(error)
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(
                f"That command is on cooldown for `{error.retry_after:,.0f}` more seconds!"
            )
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.reply("make sure to enter a required argument")

        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.reply("some error happened give me enough permissions for that ")
        if isinstance(error, commands.NotOwner):
            await ctx.reply("you are not my owner ")

    @commands.Cog.listener("on_command")
    async def on_command(self, ctx):
        channel = self.bot.get_channel(805355006551130122)
        embed = discord.Embed()
        embed.set_author(name="Command invoked")
        embed.add_field(name="Command", value=f"``{ctx.command}``")
        embed.add_field(name="Author", value=f"``{ctx.author}``")
        embed.add_field(name="Author ID", value=f"``{ctx.author.id}``")
        embed.add_field(name="Channel", value=f"``{ctx.channel}``")
        embed.add_field(name="Channel ID", value=f"``{ctx.channel.id}``")
        embed.add_field(name="Guild", value=f"``{ctx.guild}``")
        embed.add_field(name="Guild ID", value=f"``{ctx.guild.id}``")
        await channel.send(embed=embed)

    @commands.Cog.listener("on_slash_command")
    async def on_slash_command(self, ctx):
        channel = self.bot.get_channel(805355006551130122)
        embed = discord.Embed()
        embed.set_author(name="Slash Command invoked")
        embed.add_field(name="Command", value=f"``{ctx.command}``")
        embed.add_field(name="Author", value=f"``{ctx.author}``")
        embed.add_field(name="Author ID", value=f"``{ctx.author.id}``")
        embed.add_field(name="Channel", value=f"``{ctx.channel}``")
        embed.add_field(name="Channel ID", value=f"``{ctx.channel.id}``")
        embed.add_field(name="Guild", value=f"``{ctx.guild}``")
        embed.add_field(name="Guild ID", value=f"``{ctx.guild.id}``")
        await channel.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Events(bot))