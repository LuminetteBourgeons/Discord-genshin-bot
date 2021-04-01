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

owner= [
  809244553768861706, #brianynne
  743042741461712897  #luminette
]

presence= [
    discord.Activity(type=discord.ActivityType.watching, name=("Childe ❤️")),
    discord.Activity(type=discord.ActivityType.playing, name=("with Xiao")),
    discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'minet, '")),
]

love_u = [ #buat bucinan ehe
  'Love you', 
  'love u', 
  'love you', 
  'Love u'
]

'''
luminet = [
  "Luminette", 
  "luminette", 
  "Luminet", 
  "luminet", 
  "Minet", 
  "minet"
]
'''

curse_words = [
  "fuck", "FUCK",
  "shit", "SHIT",
  "piss", "PISS",
  "dick", "DICK",
  "cock", "COCK",
  "asshole", "ASSHOLE",
  "bitch", "BITCH",
  "cunt", "CUNT",
  "anjing", "ANJING",
  "bangsat", "BANGSAT",
  "ngentot", "NGENTOT",
  "peepee", 
  "poopoo", #idek why
  "pussy", "PUSSY",
  "kontol", "KONTOL",
  "memek", "MEMEK",
  "memeq", "MEMEQ"
]

shut = [
  "Language.", "Hey! >:(", "Ngomongnya ya >:(", "Heh! >:("
]

answer = [
  "hm?", "ya?", "apa?"
  ]

PREFIX = [
  "Minet, ",
  "Minet,",
  "minet, ",
  "minet,"
]

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
    print('Luminette is online.')

@bot.command
async def help(ctx):
    embed = discord.Embed(title="Luminette's bot commands:", description="prefix: `minet,`, `Minet,`", color=discord.Color.orange())
    embed.set_thumbnail(url=bot.icon_url)
    await ctx.send(embed=embed)

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
async def userinfo(ctx, user: discord.User = None):
    pass
    if user is None:
        user = ctx.author
    name = f'{user.name}'
    nick = f'{user.nick}'
    if nick is None:
     nick = name
    id = f'`{user.id}`'
    status = f'`{user.status}`' #masih error 
    voice_state = None if not user.voice else user.voice.channel
    voice = f'`{voice_state}`'
    activity = f'`{user.activity}`'
    role = f'{user.top_role.name}'
    if role == "@everyone":
     role = "None"
    icon = f'{user.avatar_url}'
    embed = discord.Embed(title=name + "'s Information",
                          color=discord.Color.orange())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="User Nickname", value=nick, inline=True)
    embed.add_field(name="User ID", value=id, inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="In Voice", value=voice, inline=True)
    embed.add_field(name="In Activity", value=activity, inline=True)
    embed.add_field(name="Highest Role", value=role, inline=True)
    embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
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
async def dm(ctx, user: discord.User, *, value):
  await user.send(f"**{value}**")
  await user.send(f"||Sent by {ctx.author.name}||")
  await ctx.send("DM sent!")

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
    embed.set_footer(icon_url=f'{bot.user.avatar_url}')
    seconds = 0
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} day(s)"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hour(s)"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minute(s)"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} second(s)"
    if seconds == 0:
        embed.add_field(name='Warning',
                        value='Please specify a proper duration :(')
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
        await ctx.author.send(f"Hi, you asked me to remind you about {reminder} {counter} ago.")
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

    for i in curse_words:
      if i in message.content.lower():
        print(f"{message.content}, said {message.author}")
        await asyncio.sleep(2)
        await message.delete()
        await message.channel.send(random.choice(shut))
        bot.dispatch('profanity', message, i)
        return
        await bot.process_commands(message)
    
    if any(word in message.content for word in love_u):
        if message.author.id == 236823518233362442:
            await message.add_reaction('❤️')
    
    if message.content.lower().startswith ("Tes"):
      me = await bot.get_user_info(message.author_id)
      await bot.send_message(me, "Tis")

'''
    if any(word in message.content for word in luminet):
        await asyncio.sleep(1)
        await message.channel.send(random.choice(answer))
        await bot.process_commands(message)
'''

@bot.event
async def on_profanity(message, word):
   channel = bot.get_channel(825190542115078164)
   embed = discord.Embed(title="Profanity Alert!",description=f"{message.author.name} just said ||{word}||", color=discord.Color.orange()) 
   await channel.send(embed=embed)

@bot.command()
async def pstart(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.start()
    await ctx.send("Auto presence-changing started.")
  else:
    await ctx.send("You are not allowed to use this command!")


@bot.command()
async def pstop(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.cancel()
    await ctx.send("Auto presence-changing has stopped.")
  else:
    await ctx.send("You are not allowed to use this command!")

#keep_alive()
bot.run(os.getenv('TOKEN'))
