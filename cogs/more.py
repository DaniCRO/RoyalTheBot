import discord
import random
from discord.ext import commands
import logging
import traceback
from datetime import datetime
import asyncio
import os
import aiohttp
from discord import opus
from asyncio import sleep
import datetime


class More():
	def __init__(self, bot):
		self.bot = bot







	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.command()
	async def feedback(self, ctx, *, feedback=None):
		'''Send your feedback to the bot creators
		-------------------
		Ex:
		r!feedback [feedback]'''
		if feedback is None:
			await ctx.send('Hey, please do `r!feedback <feedback>`')
		if feedback is not None:
			await self.bot.get_guild(453974498421506062).get_channel(478504533480177684).send(f'{ctx.author} ({ctx.author.id}) reported: {feedback}')
			await ctx.send('Your feedback was reported to the team')










	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.command()
	async def bug(self, ctx, *, bug=None):
		'''Report a bug
		-------------------
		Ex:
		r!bug [bug]'''
		if bug is None:
			await ctx.send('Hey, please do `r!bug <bug>`')
		if bug is not None:
			await self.bot.get_guild(453974498421506062).get_channel(478504558163787776).send(f'{ctx.author} ({ctx.author.id}) reported: {bug}')
			await ctx.message.channel.send('Your problem was reported to the team')















































def setup(bot):
        bot.add_cog(More(bot))
