import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from keep_alive import keep_alive
import os, asyncio
from random import choice

orange= discord.Colour.dark_red()

presence= [
    discord.Activity(type=discord.ActivityType.playing, name=("Develop by Luminette")),
    discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'tao! '")),
    discord.Activity(type=discord.ActivityType.playing, name=("✨new prefix: '+ '✨")),
    discord.Activity(type=discord.ActivityType.watching, name=("Qiqi"))
]

PREFIX = [
  "Tao! ",
  "Tao!",
  "tao! ",
  "tao!",
  "+ ",
  "+"
]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

Hu_tao = ['hu tao', 'hutao']

bot.remove_command('help') 

@bot.command()
async def help(ctx):
  pass

@bot.command()
async def modhelp(ctx):
  pass

@bot.command()
async def invite (ctx):
  pass

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=("no one")))
  print('Hu Tao is online.')
  
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.send(f'Command not found! Use `+help` for the list of commands!', delete_after=3)
    return
  elif isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(title="Error!", description="You are missing the permission `" + ", ".join(error.missing_perms) + "` to execute this command!", color=discord.Colour.red())
    await ctx.send(embed=embed, delete_after=7)
  elif isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="Error!",description=str(error).capitalize(), color=discord.Colour.red())
    await ctx.send(embed=embed, delete_after=7)
  elif isinstance(error, commands.ChannelNotFound):
    await ctx.send(f'Channel not found!', delete_after=7)
    return
  elif isinstance(error, commands.MemberNotFound):
    await ctx.send(f'Member not found!', delete_after=7)
    return
  raise error

@bot.event
async def on_member_join(member):
  pass

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)
  if any(word in message.content for word in Hu_tao):
    await message.channel.send('Wangy wangy~ :heart:')
    await bot.process_commands(message)

@bot.event
async def on_command(ctx):
  pass
@bot.event
async def on_command_completion(ctx):
  pass

@bot.command(aliases=['echo'])
async def say(ctx, *, msg):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def servers(ctx):
  pass

@tasks.loop(minutes=5)
async def presence_change():
  await asyncio.sleep(10)
  await bot.change_presence(activity=choice(presence))
@presence_change.before_loop
async def presence_change_before():
  await bot.wait_until_ready()
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

@bot.command()
async def shutdown(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.send('shutting down... good night...')
    await bot.close()

extensions = [ 
  'cogs.miscellaneous', 
  'cogs.mod', 
  'cogs.reminder', 
  'cogs.voice', 
  'cogs.info'  
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
keep_alive()
bot.run(os.getenv('TOKEN'))
