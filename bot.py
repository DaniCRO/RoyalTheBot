import discord
import random
import datetime
import traceback
import aiohttp
import asyncio
import json
import async_timeout
from random import randint
from discord.ext import commands
import logging


logging.basicConfig(level='INFO')
bot = commands.Bot(case_insensitive=True, command_prefix='r!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logging in as', bot.user.name)

@bot.listen()
async def on_message(message):
    if message.content.lower() == '<@483932645366038529>' and message.author != bot.user:
        await message.channel.send('**My prefix is `r!` | Use `r!help` for show commands.**')
    else:
        await bot.process_command(message)

@bot.command(aliases= ["sinfo"])
async def serverinfo(ctx):
	"""Get the server info"""
	em = discord.Embed(color=discord.Colour.blue())
	em.add_field(name=':paintbrush: Name', value=f'{ctx.author.guild.name}', inline=False)
	em.add_field(name=':crown: Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=False)
	em.add_field(name=':mountain_snow: Icon', value='Do r!servericon', inline=False)
	em.add_field(name=':family_mwgb: Roles', value='Do r!serverroles', inline=False)
	em.add_field(name=':bust_in_silhouette: Members', value=f'{ctx.guild.member_count}', inline=False)
	em.add_field(name=':clock1: Created at', value=ctx.guild.created_at, inline=False)
	em.set_thumbnail(url=ctx.guild.icon_url)
	await ctx.send(embed=em)

@bot.command(aliases=['sroles'])
async def serverroles(ctx):
	"""Get the server roles"""
	em = discord.Embed(color=discord.Colour.blue())
	em.add_field(name=f'Server Roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for g in ctx.guild.roles))
	await ctx.send(embed=em)

@bot.event
async def on_command_error(ctx, error):
    if ctx.author.bot is True:
        return
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send('The command was not found')
    print(f'{ctx.author} used the command {ctx.command} and got the error  {error}')
    await ctx.send(f'Error | {error}')

@bot.command(aliases= ["whois"])
async def userinfo(ctx, member: discord.Member=None):
    if member is None:
        member = (ctx.author)
    embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
    embed.set_author(name="Who is?")
    embed.add_field(name=":bust_in_silhouette: | Name", value=member.name)
    embed.add_field(name=":id: | ID", value=member.id)
    embed.add_field(name=":robot: | Bot?", value=member.bot)
    embed.add_field(name=":atm: | Tag", value=member.discriminator)
    embed.add_field(name=":eject: | Highest role that he owns", value=member.top_role)
    embed.add_field(name=":pencil2: | Nickname", value=member.nick)
    embed.add_field(name=":inbox_tray: | Joined", value=member.joined_at)
    embed.add_field(name=":clock1: | Created at", value=member.created_at)
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="An amazing bot, these are the commands:", color=0xeee657)

    embed.add_field(name="r!add X Y", value="Adds the number**X** with the number **Y**", inline=False)
    embed.add_field(name="r!multiply X Y", value="Multiplies the numbers**X** and **Y**", inline=False)
    embed.add_field(name="r!cat", value="Gives you a gif/photo with a cat to make you happy :)", inline=False)
    embed.add_field(name="r!info", value="Gives you some info about this bot", inline=False)
    embed.add_field(name="r!help", value="Gives this message", inline=False)
    embed.add_field(name="r!userinfo", value="Gives the profile information about you, or other users", inline=False)
    embed.add_field(name="r!serverroles", value="Shows the roles that exist on the server.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Do you want me to invite me into your server?", description="Ok", color=0xeee657)

       # give users a link to invite this bot to their server
    embed.add_field(name="Invite me into your server!", value="[Invite link](<https://discordapp.com/oauth2/authorize?&client_id=483932645366038529&scope=bot&permissions=0>)")

    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    """Generates a random image of a kitty"""
    async with aiohttp.ClientSession() as cs:
        async with cs.get('http://aws.random.cat/meow') as r:
            res = await r.json()
        embed = discord.Embed(color=0x000000)
        embed.title = "What a cute :cat:"
        embed.set_image(url=res['file'])
        embed.set_footer(text=f"Kitty")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def sal(ctx):
    await ctx.send('cf')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Info", description="The best bot ever. :)", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Creator", value="<@160068544409763840>")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Number of servers that this bot is in", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    t = await ctx.send('Pong!, Calculating...')
    await asyncio.sleep(1)
    await t.edit(content=f'```My ping is : {ctx.bot.latency * 1000:.0f} MS !```')

client.run(os.getenv('TOKEN'))
