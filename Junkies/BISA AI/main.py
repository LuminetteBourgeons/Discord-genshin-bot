import discord
import nacl
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from discord.utils import get
import os
import random
from random import choice
import asyncio
from asyncio import sleep
from keep_alive import keep_alive

owner= [
  809244553768861706, #potatish
  743042741461712897  #luminette
]

presence= [
  discord.Activity(type=discord.ActivityType.playing, name=("Develop by Aisha")),
  discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'ai, '")),
  discord.Activity(type=discord.ActivityType.watching, name=("Student Ambassadors"))
]

PREFIX = [
  "Ai, ",
  "Ai,",
  "ai, ",
  "ai,",
  "+ ",
  "+"
]

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None)

bot.remove_command('help') 

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="BISA AI bot's commands:", description="prefix: `Ai, `, `ai, `\nDevelop by Aisha `Luminette#0666`\n<https://github.com/LuminetteBourgeons/BISA.AI_bot/tree/main>", colour=discord.Color.blurple())
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="__Bot's invitation link:__", value="https://discord.com/api/oauth2/authorize?client_id=829876995058958377&permissions=8&scope=bot\n*as Administrator*", inline=False)
    embed.add_field(name="__Bot owner only__", value="***Auto Presence Changing:***\npstart/pstop\n", inline=True)
    embed.add_field(name="__Admins__", value="***Presence Changing:***\nsetonline\nsetidle\nsetdnd\nsetinv\nactplaying\nactlistening\nactwatching\nactcompeting\n***Making Embed:***\nembedevent `(terikat dengan channel #bisa-ai-event)`\nembed\n***Say:***\nsay\n***Dm:***\ndm\n***Warn:***\nwarn", inline=True)
    embed.add_field(name="__General__", value="***Shows User's Avatar:***\navatar\n***Shows User's Information:***\nuserinfo\n***Shows Server's Icon***\nservericon\n***Shows Server's Information:***\nserverinfo\n***Reminder:***\nreminder", inline=True)
    embed.add_field(name='__Warning!__', value="General can't use Admins and Bot Owner's commands!\nAdmins can't use Bot Owner's commands!", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
    print('AI is online.')

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
async def embedevent(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    await ctx.send('Enter a title')
    title = await bot.wait_for('message', check=check)
    await ctx.send('Enter a description')
    desc = await bot.wait_for('message', check=check)
    embed = discord.Embed(title=title.content, description=desc.content, color=discord.Colour.blurple())
    message_channel = bot.get_channel(829879666881200149)
    print(f"Got channel {message_channel}")
    await message_channel.send(embed=embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    await ctx.send('Enter a title')
    title = await bot.wait_for('message', check=check)
    await ctx.send('Enter a description')
    desc = await bot.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content, color=discord.Colour.blurple())
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setonline(ctx):
    await ctx.bot.change_presence(status=discord.Status.online)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's status to",
                          description='`Online`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setidle(ctx):
    await ctx.bot.change_presence(status=discord.Status.idle)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's status to",
                          description='`Idle`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setdnd(ctx):
    await ctx.bot.change_presence(status=discord.Status.dnd)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's status to",
                          description='`Do not disturb`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def setinv(ctx):
    await ctx.bot.change_presence(status=discord.Status.invisible)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's status to",
                          description='`Invisible`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actplaying(ctx, *, name):
    await ctx.bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name=name)
    )
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's activity to",
                          description=f'`playing {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actlistening(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's activity to",
                          description=f'`listening {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actwatching(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's activity to",
                          description=f'`watching {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actcompeting(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.competing, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set BISA AI bot's activity to",
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
                          colour=discord.Colour.blurple())
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
                          color=discord.Color.blurple())
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
            color=discord.Colour.blurple(),
            title=f'{ctx.author.name}',
            description='Please specify the user you want to warn\n Use:`ai, warn @user`')
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
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@bot.command()
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
  else:
    await ctx.send("You're not in a voice channel, connect to a voice channel to use this command!")


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

keep_alive()
bot.run(os.getenv('TOKEN'))
