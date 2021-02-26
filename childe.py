# WORK IN PROGRESS
# cita-citanya mau jadi bot serba bisa :)

import discord
from discord.ext import commands, tasks
# from keep_alive import keep_alive  
import asyncio
from asyncio import sleep as s
import datetime as dt
import os


bot = commands.Bot("ch!")

target_channel_id = 807495144093384724


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Luminette ❤️"))
    print('{0.user} is home!'.format(bot))

@bot.command()
async def sreminder(ctx, time: int, *, msg):
    while True:
        await s(time)
        await ctx.send(f'{msg}, {ctx.author.mention}')

@bot.command()
async def hreminder(ctx, time: int, *, msg):
    while True:
        await s(60*time)
        await ctx.send(f'{msg}, {ctx.author.mention}')

@bot.command()
@commands.is_owner()
async def say(ctx,* ,msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    if message.content.startswith('hello'):
        await message.channel.send('Hi, {0.author.mention} !'.format(message))
        await bot.process_commands(message)

    if message.content.startswith('Hello'):
        await message.channel.send('Hi, {0.author.mention} !'.format(message))
        await bot.process_commands(message)

    if message.content.startswith('Childe?'):
        await message.channel.send('Hey girlie, hold still')
        await bot.process_commands(message)

    if message.content.startswith('Love you'):
      if message.author.id == 743042741461712897:
        await message.channel.send(':heart: <@743042741461712897>')
        await bot.process_commands(message)
      else:
        await message.channel.send("I'm Luminette's, sorry ;)")
        await bot.process_commands(message)

@tasks.loop(hours=24)
async def email_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Have you check your email, sweetie?")

@email_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Reminding Email started.")


email_once_a_day.start()
# keep_alive()
bot.run(os.getenv('TOKEN'))
