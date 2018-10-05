from discord.ext import commands
from .utils import checks, formats
from .utils.paginator import HelpPaginator, CannotPaginate
import discord
from collections import OrderedDict, deque, Counter
import os, datetime
import asyncio
import copy
import unicodedata
import inspect



class Meta:
    """Commands for utilities related to Discord or the Bot itself."""

    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)

    @bot.command()
async def help(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.add_field(name='★Fun★', value='`8ball, lenny, respect, ping, poll, choose, dog, cat, doge, say', inline=True)
    em.add_field(name='★Moderation★', value='`kick, ban, purge, botnick`', inline=True)
    em.add_field(name='★Utility★', value='`servericon, serverroles, serverinfo, userinfo, servericon, avatar, support, about, calculate, emoji, invite', inline=True)
    em.add_field(name='★Owner-Only★',value='`eval, shutdown, reload, load, unload`', inline=True)
    em.set_footer(text="Use 'r!' before each command", icon_url=ctx.me.avatar_url)
    em.set_thumbnail(url=ctx.me.avatar_url)
    await ctx.send(embed=em)



    @commands.command(aliases=['char'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def charinfo(self, ctx, *, characters: str):
        """Shows you information about a number of characters.
        -------------------
		Ex:
		r!charinfo :wave:
        """

        def to_string(c):
            digit = f'{ord(c):x}'
            name = unicodedata.name(c, 'Name not found.')
            return f'**{c}** | ``\\U{digit:>08}`` | {name}'
        msg = '\n'.join(map(to_string, characters))
        if len(msg) > 750:
            return await ctx.send('Output too long to display.')
        await ctx.send(msg)









def setup(bot):
    bot.add_cog(Meta(bot))
