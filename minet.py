#develop by Brianynne#0202(+Luminette#0666)
#WORK IN PROGRESS

import discord
#import nacl
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from discord.utils import get
import os
import random
from random import choice
import asyncio
from asyncio import sleep
#from keep_alive import keep_alive

presence = 
[
    discord.Activity(type=discord.ActivityType.watching, name=("Primordial World")),
    discord.Activity(type=discord.ActivityType.watching, name=("Childe ❤️")),
    discord.Activity(type=discord.ActivityType.watching, name=("Alvard galak")),
    discord.Activity(type=discord.ActivityType.playing, name=("with Mayonese")),
    discord.Activity(type=discord.ActivityType.playing, name=("with Moderators")),
    discord.Activity(type=discord.ActivityType.playing, name=("Develop by luminet")),
    discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'net, '"))
    discord.Activity(type=discord.ActivityType.competing, name=("with Paidoru")),
    discord.Activity(type=discord.ActivityType.competing, name=("#💬・public-chat")),
]

love_u = #buat bucinan ehe 
[
  'Love you', 
  'love u', 
  'love you', 
  'Love u'
]

luminet = 
[
  "Luminette", 
  "luminette", 
  "Luminet", 
  "luminet", 
  "Minet", 
  "minet"
]

curse_words = 
[
  "fuck",
  "shit", 
  "piss", 
  "dick", 
  "asshole",
  "bitch", 
  "cunt",
  "anjing", 
  "bangsat", 
  "ngentot", 
  "peepee", 
  "poopoo", #idek why
  "pussy", 
  "damn"
]

shut = 
[
  "Language!!", "Hey! >:(", "Hey, watch it.", "Ngomongnya ya! >:(", "Heh! >:("
]
answer = ["hm?", "ya?", "apa?", "ada apa?"]

bot = commands.Bot(command_prefix="net, ", case_insensitive=True)


@bot.event
async def on_ready():
    await bot.change_presence(activity=
                              discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
    await asyncio.sleep(5)
    await bot.change_presence(activity=
                              discord.Activity(type=discord.ActivityType.competing, name=("development")))
    print('Luminette is online.')

@loop(minutes=5)
async def presence_change():
    await asyncio.sleep(10)
    await bot.change_presence(activity=choice(presence))
    print("Change presence")

@presence_change.before_loop
async def presence_change_before():
    await bot.wait_until_ready()

@bot.command()
@commands.has_permissions(administrator=True)
async def setonline(ctx):
    await ctx.bot.change_presence(status=discord.Status.online)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's status to",
                          description='`Online`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setidle(ctx):
    await ctx.bot.change_presence(status=discord.Status.idle)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's status to",
                          description='`Idle`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setdnd(ctx):
    await ctx.bot.change_presence(status=discord.Status.dnd)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's status to",
                          description='`Do not disturb`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setinv(ctx):
    await ctx.bot.change_presence(status=discord.Status.invisible)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's status to",
                          description='`Invisible`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actplaying(ctx, *, name):
    await ctx.bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name=name)
    )
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's activity to",
                          description=f'`playing {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actlistening(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's activity to",
                          description=f'`listening {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actwatching(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's activity to",
                          description=f'`watching {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actcompeting(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.competing, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Luminette's activity to",
                          description=f'`competing in {name}`')
    await ctx.send(embed=embed)
 
@bot.command()
async def avatar(ctx, user: discord.User = None):
    pass
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f'{user.name}\'s avatar.',
                          url=f"{user.avatar_url}",
                          colour=discord.Colour.orange())
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
    
@bot.command()
async def servericon(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name} server icon.',
                          url=f"{ctx.guild.icon_url}",
                          colour=discord.Colour.orange())
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    name = f'{ctx.guild.name}'
    owner = f'<@{ctx.guild.owner_id}>'
    id = f'`{ctx.guild.id}`'
    region = f'`{ctx.guild.region}`'
    memberCount = f'`{ctx.guild.member_count}`'
    icon = f'{ctx.guild.icon_url}'
    embed = discord.Embed(title=name + " Server Information",
                          color=discord.Color.orange())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Server Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, user: discord.User = None):
    if user is None:
        embed = discord.Embed(
            color=discord.Colour.orange(),
            title=f'Heh, {ctx.author.name}',
            description='Siapa yang mau di warn >:(\n Use:`net, warn @user`')
        await ctx.send(embed=embed)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title=f' {user.name}, you have been warned!',
                          description=f'by {ctx.author.name}')
    await ctx.send(embed=embed)


@bot.command()
async def reminder(ctx, time, *, reminder):
    embed = discord.Embed(color=discord.Colour.orange())
    embed.set_footer(icon_url=f"{bot.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(
            name='Warning',
            value='Please specify what do you want me to remind you about.')
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Warning',
                        value='Please specify a proper duration :(')
    elif seconds < 300:
        embed.add_field(
            name='Warning',
            value=
            'You have specified a too short duration!\nMinimum duration is 5 minutes.'
        )
    elif seconds > 7776000:
        embed.add_field(
            name='Warning',
            value=
            'You have specified a too long duration!\nMaximum duration is 90 days.'
        )
    else:
        await ctx.send(
            f"Alright, I will remind you about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send(
            f"Hi, you asked me to remind you about {reminder} {counter} ago.")
        return
    await ctx.send(embed=embed)


@bot.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()
    await asyncio.sleep(5)
    await ctx.message.delete()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await asyncio.sleep(5)
    await ctx.message.delete()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    if any(word in message.content for word in curse_words):
        await asyncio.sleep(2)
        await message.delete()
        await message.channel.send(random.choice(shut))
        await bot.process_commands(message)

    if any(word in message.content for word in luminet):
        await asyncio.sleep(1)
        await message.channel.send(random.choice(answer))
        await bot.process_commands(message)

    if any(word in message.content for word in love_u):
        if message.author.id == 236823518233362442:
            await message.add_reaction('❤️')


presence_change.start()
#keep_alive()
bot.run(os.getenv('TOKEN'))
