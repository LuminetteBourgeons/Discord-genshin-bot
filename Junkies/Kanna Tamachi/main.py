import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
import os, os.path, asyncio
from PIL import Image, ImageFont, ImageDraw
from random import choice

#welcome text hex = F097AD
#status         =855806495344820234
#commands       =855806527730221096
#commands-error =855806576015310868
#warn-log       =855806705522311210

orange=0xe68a89

presence= [
    discord.Activity(type=discord.ActivityType.competing, name=("Develop by Luminette")),
    discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'k! '")),
    discord.Activity(type=discord.ActivityType.playing, name=("✨new prefix: '+ '✨")),
    discord.Activity(type=discord.ActivityType.watching, name=("Tamadachi ❤️")),
    discord.Activity(type=discord.ActivityType.playing, name=("with Tamadachi"))
]

PREFIX = [
  "K! ", 
  "K!", 
  "k! ", 
  "k!", 
  "+ ", 
  "+"
  ]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

bot.remove_command('help') 

@bot.command()
async def help(ctx):
  pass

@bot.command()
async def invite (ctx):
  embed=discord.Embed(title="__Invite me to your server!__", description="[Click here]https://discord.com/api/oauth2/authorize?client_id=855622760033419294&permissions=8&scope=bot)\n*as Administrator*\n", colour=orange)
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
  channel = bot.get_channel(855806495344820234)
  await channel.send('Rebooting')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
  print('Kanna is online.')
  
@bot.event
async def on_command_error(ctx, error):
  pass

@bot.event
async def on_member_join(member):
  if member.guild.id == 831356457554280449:
    channel = bot.get_channel(831360289274069012)
    img = Image.open("Welcome.png")
    font = ImageFont.truetype("Poppins-Medium.ttf", 28)
    draw = ImageDraw.Draw(img)
    text = ("Welcome,\n {}!\n Enjoy your stay~".format (member.name))
    draw.text((290,610), text, (240, 151, 173), font=font)
    img.save("./welcome/{}.png".format (member.name))
    embed=discord.Embed(title='Hello, Tamadachi ❤️', description=':coffee: Welcome to Tamadachi Café~\n\nRemember to check out <#768081907807420435> and react with :white_check_mark: to get access to the server!\n\n[If you have any questions or concerns, feel free to contact the Moderators or Champions]\n\nHope you enjoy your stay~',colour=orange)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send (embed=embed, file=discord.File("./welcome/{}.png".format (member.name)))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)

@bot.event
async def on_command(ctx):
  channel = bot.get_channel(855806527730221096)
  embed = discord.Embed(title=f"{ctx.author.name} used a command!", description=f"{ctx.message.content}",colour=discord.Color.orange())
  await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
@bot.event
async def on_command_completion(ctx):
  channel = bot.get_channel(855806527730221096)
  embed = discord.Embed(title=f"Completed {ctx.author.name}'s command!", description=f"{ctx.message.content}",colour=discord.Color.gold())
  await channel.send(embed=embed)

@bot.command(aliases=['echo'])
async def say(ctx, *, msg):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def servers(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.send("__**Kanna's active servers:**__")
    activeservers = bot.guilds
    for guild in activeservers:
      await ctx.send(f'Server name:`{guild.name}`,\nServer ID:`{guild.id}`,\nServer Owner:`{guild.owner}`\nOwner ID :`{guild.owner.id}`\nMembers: `{guild.member_count}`')
      await ctx.send('––––––––––––––––––––––––––––––––––––––––––––––––')

@tasks.loop(minutes=5)
async def presence_change():
  await asyncio.sleep(10)
  await bot.change_presence(activity=choice(presence))
  channel = bot.get_channel(854593444072390657)
  await channel.send('Changing Presence')
  print("Changing Presence")
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
  'cogs.info',
  'cogs.fun'
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
keep_alive()
bot.run(os.getenv('TOKEN'))
