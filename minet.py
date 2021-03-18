#:)
import discord
from discord.ext import commands
#import nacl
import os
import random
import asyncio
from asyncio import sleep
from keep_alive import keep_alive
import datetime

love_u = ['Love you', 'love u','love you', 'Love u']
luminet =["Luminette", "luminette", "Luminet", "luminet", "minet", "Minet"]
curse_words = ["fuck", "Fuck", "FUCK", "Shit", "SHIT", "shit", "Piss", "piss", "Dick", "dick", "asshole", "Asshole", "ASSHOLE", "Bitch", "bitch", "Cunt", "cunt", "Anjing", "anjing", "ANJING", "bangsat", "Bangsat", "ngentot", "Ngentot", "peepee", "poopoo", "pussy", "Pussy", "damn", "DAMN", "Damn"]
shut = [
  "Language!!",
  "Hey! >:(",
  "Hey, watch it.",
  "Ngomongnya ya! >:(",
  "Heh! >:("
]
answer =[
  "hm?", 
  "ya?", 
  "apa?", 
  "ada apa?"
]


bot = commands.Bot("net, ")

@bot.event
async def on_ready():
    print('Luminette is online.')

@bot.command()
async def avatar(ctx, user: discord.User = None):
    pass
    if user is None:
     user = ctx.author
    embed = discord.Embed(title=f'{user.name}\'s avatar.', url=f"{user.avatar_url}" , colour=discord.Colour.orange())
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed) 

@bot.command()
async def warn(ctx, user: discord.User = None):
    if user is None:
      embed = discord.Embed(color=discord.Colour.orange(), title=f'Heh, {ctx.author.name}', description='Siapa yang mau di warn >:(\n Use:`net, warn @user`')
      await ctx.send(embed=embed)
    embed = discord.Embed(color=discord.Colour.orange(), title=f' {user.name}, you have been warned!', description=f'by {ctx.author.name}')
    await ctx.send(embed=embed)

@bot.command()
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=discord.Colour.orange())
    embed.set_footer(icon_url=f"{bot.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') 
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
      embed.add_field(name='Warning',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
    elif seconds > 7776000:
        embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send(f"Hi, you asked me to remind you about {reminder} {counter} ago.")
        return
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx,* ,msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
@commands.has_permissions(administrator=True)
async def setonline(ctx):
    await ctx.bot.change_presence(status=discord.Status.online)
    await ctx.message.channel.send('Set status to `online`')

@bot.command()
@commands.has_permissions(administrator=True)
async def setidle(ctx):
    await ctx.bot.change_presence(status=discord.Status.idle)
    await ctx.message.channel.send('Set status to `idle`')

@bot.command()
@commands.has_permissions(administrator=True)
async def setdnd(ctx):
    await ctx.bot.change_presence(status=discord.Status.dnd)
    await ctx.message.channel.send('Set status to `do not disturb`')

@bot.command()
@commands.has_permissions(administrator=True)
async def setinv(ctx):
    await ctx.bot.change_presence(status=discord.Status.invisible)
    await ctx.message.channel.send('Set status `invisible`')

@bot.command()
@commands.has_permissions(administrator=True)
async def actplaying(ctx,* ,name):
    await ctx.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=name))
    await ctx.send(f"Set activity `playing {name}`")

@bot.command()
@commands.has_permissions(administrator=True)
async def actlistening(ctx,* ,name):
    await ctx.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=name))
    await ctx.send(f"Set activity `listening {name}`")

@bot.command()
@commands.has_permissions(administrator=True)
async def actwatching(ctx,* ,name):
    await ctx.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=name))
    await ctx.send(f"Set activity `watching {name}`")

@bot.command()
@commands.has_permissions(administrator=True)
async def actcompeting(ctx,* ,name):
    await ctx.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.competing,
                name=name))
    await ctx.send(f"Set activity `competing in {name}`")

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
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
      if message.author.id == 236823518233362442: #id siapa hayo 
       await message.add_reaction ('❤️')

keep_alive()
bot.run(os.getenv('TOKEN'))
