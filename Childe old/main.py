import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from keep_alive import keep_alive
#import nacl
import os, asyncio, json, random
from random import choice

presence= [
  discord.Activity(type=discord.ActivityType.playing, name=("Develop by Luminette")),
  discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'ch! '")),
  discord.Activity(type=discord.ActivityType.playing, name=("with Luminette")),
  discord.Activity(type=discord.ActivityType.competing, name=("with Paidoru >:(")),
  discord.Activity(type=discord.ActivityType.watching, name=("Luminette ❤️")),
  discord.Activity(type=discord.ActivityType.playing, name=("minet bucin sm mayo")),
  discord.Activity(type=discord.ActivityType.watching, name=("Primordial World"))
]

PREFIX = [
  "Ch! ",
  "Ch!",
  "ch! ",
  "ch!",
  "+ ",
  "+"
]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

bot.regionals = { 'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 
                  'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
                  'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
                  'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 
                  'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
                  'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
                  'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 
                  'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
                  'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
                  'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 
                  'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
                  'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
                  'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 
                  'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
                  'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
                  'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 
                  'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
                  'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
                  's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 
                  't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
                  'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
                  'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 
                  'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
                  'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
                  'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 
                  'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
                  '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
                  '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', 
                  '8': '8⃣', '9': '9⃣', '!': '\u2757', '?': '\u2753'}

bot.ball = ['It is certain', 
            'It is decidedly so', 
            'Without a doubt', 
            'Yes definitely', 
            'You may rely on it',
            'As I see it, yes', 
            'Most likely', 
            'Outlook good', 
            'Yes', 
            'Signs point to yes',
            'Reply hazy try again', 
            'Try ask Zhongli about this', 
            'Ask again later', 
            'Better not tell you now', 
            'Cannot predict now', 
            'Oh, sorry... Please ask again, I lost myself in your eyes.',
            'Don\'t count on it, comrade', 
            'My reply is no', 
            'My sources say no', 
            'Outlook not so good', 
            'Very doubtful']

bot.remove_command('help') 

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="__*Childe's commands:*__", description="Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨\n🧡 Develop by: `Luminette#9466`, `Potatish#0666`\n<:PaimonHehe:843373207130079232> The next generation of __Paidoru__ (`Paimon#7192`) by `Nawaytes~#2470`\n‎‎‎", colour=discord.Color.orange())
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
    embed.add_field(name="<:Chchibi:843379361138737182>__Bot's invitation link:__<:Chchibi:843379361138737182>", value="https://discord.com/api/oauth2/authorize?client_id=806793987876192268&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1&scope=bot\n*as Administrator*\n\n***List of Commands:***", inline=False)
    embed.add_field(name="__Admins commands:__", value="***Presence Changing:***\n・set<status>\n`ex: setidle`\n・act<activity> <activity name>\n‏‏‎`ex: actlistening music`\n‏‏‎‎‏‏‎***Moderations:***\n‏‏‎‎‏‏‎・warn @user\n‏‏‎‎‏‏‎・kick @user\n‏‏‎‎‏‏‎・ban @user\n‏‏‎‎‏‏‎・mute @user\n‏‏‎‎‏‏‎・unmute @user\n‏‏‎‎‏‏‎***Making Embed:***\n‏‏‎‎‏‏‎・embed\n‏‏‎‎‏‏‎‏‏‎‎‏‏‎`uses JSON`\n‏‏‎‎‏‏‎‏‏‎‎‏‏‎<https://discohook.org/> \n‏‏‎‎‏‏‎***DM***\n‏‏‎‎‏‏‎・dm @user <value>\n‏‏‎‎‏‏‎‏‏‎‎‏‏‎`modhelp coming soon :)`\n‏‏‎‎‏‏‎***Delete Messages***\n‏‏‎‎‏‏‎・delete <# of messages>\n‏‏‎‎‏‏‎・delete <# of messages> @user\n‏‏‎‎‏‏‎‏‏‎‎‏‏‎has a limit of 500 messages", inline=False)
    embed.add_field(name="__General commands:__", value="‏‏‎‎‏‏‎***Voice:***\n‏‏‎‎‏‏‎・join\n‏‏‎‎‏‏‎・leave\n‏‏‎‎‏‏‎・voicemute `uh... working on it`\n‏‏‎‎‏‏‎***Reminder:***\n‏‏‎‎‏‏‎・reminder <time> <something to remind you>\n‏‏‎‎‏‏‎`ex: reminder 5s cookies r ready`\n‏‏‎‎‏‏‎***Shows User's Avatar:***\n‏‏‎‎‏‏‎・avatar\n‏‏‎‎‏‏‎***Shows User's Information:***\n‏‏‎‎‏‏‎・userinfo\n‏‏‎‎‏‏‎***Shows Server's Icon***\n‏‏‎‎‏‏‎・servericon\n‏‏‎‎‏‏‎***Shows Server's Information:***\n‏‏‎‎‏‏‎・serverinfo\n\n‏‏‎\n ‎", inline=False)
    embed.add_field(name='__Warning!__', value="General can't use Admins commands!\n\n`currently working on more commands and updating weapons and artifacts, so stay tune ;)`", inline=False)
    embed.add_field(name='__Support us ❤️__', value="<https://ko-fi.com/childe_bot>", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ownerhelp(ctx):
    embed=discord.Embed(title="__Hello, Luminette 🧡__", description="My Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨", colour=discord.Color.orange())
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
    embed.add_field(name="__Your to do list on me:__", value="Fix the help command: add those `fun` command, fix the TUI\nAdd `1 piece tiara sets`\nFix weapons.json\n\n", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    channel = bot.get_channel(841614719562285086)
    await channel.send('Rebooting')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
    print('Childe is online.')
@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send(f'Command not found! Use `+help` for the list of commands!')
            return
        if isinstance(error, commands.CheckFailure):
            return
        if isinstance(error, commands.ChannelNotFound):
            await ctx.send(f'Channel not found!', delete_after=7)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f'Member not found!', delete_after=7)
            return
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'Error :(', delete_after=7)
            return
        raise error
        if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"Looks like you don't have the permission 👀")
@bot.event
async def on_member_join(member):
    if member.guild.id == 786492151058923520:
      channel = bot.get_channel(794844425956229120)
      await channel.send("Welcome, {} :heart:".format (member.mention))
    elif member.guild.id == 271215379311886336:
      channel = bot.get_channel(834013759516573707)
      await channel.send("Welcome, {} :heart:".format (member.mention)) 
    else:
      return
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hi, {0.author.mention} !'.format(message))
        await bot.process_commands(message)
    if message.content.lower().startswith('childe?'):
        await message.channel.send('Hey girlie, hold still')
        await bot.process_commands(message)
@bot.event
async def on_command(ctx):
    channel = bot.get_channel(841906846389764146)
    await channel.send(f"\n{ctx.author.name} used a command!\n`{ctx.message.content}`")

@bot.command()
@commands.has_permissions(administrator=True)
async def embed(ctx):
  await asyncio.sleep(1)
  await ctx.send('Waiting for your JSON embed... `timeout in 60 seconds.`', delete_after=5)
  message = await bot.wait_for('message', timeout=60)
  try:
    f = json.loads(str(message.content))
    embed = discord.Embed.from_dict(f)
    await asyncio.sleep(3)
    await message.delete()
    await ctx.send(embed=embed)
  except json.JSONDecodeError:
    await message.delete()
    await ctx.send('JSON ERROR', delete_after=1)
    return

@bot.command()
@commands.has_permissions(administrator=True)
async def setonline(ctx):
    await ctx.bot.change_presence(status=discord.Status.online)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's status to",
                          description='`Online`')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def setidle(ctx):
    await ctx.bot.change_presence(status=discord.Status.idle)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's status to",
                          description='`Idle`')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def setdnd(ctx):
    await ctx.bot.change_presence(status=discord.Status.dnd)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's status to",
                          description='`Do not disturb`')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def setinv(ctx):
    await ctx.bot.change_presence(status=discord.Status.invisible)
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's status to",
                          description='`Invisible`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def actplaying(ctx, *, name):
    await ctx.bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name=name)
    )
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's activity to",
                          description=f'`playing {name}`')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def actlistening(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's activity to",
                          description=f'`listening {name}`')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def actwatching(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's activity to",
                          description=f'`watching {name}`')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def actcompeting(ctx, *, name):
    await ctx.bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.competing, name=name))
    embed = discord.Embed(color=discord.Colour.orange(),
                          title="Set Childe's activity to",
                          description=f'`competing in {name}`')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def delete(ctx, limit=500, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        return await ctx.send("Please pass in an integer as limit")
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"Deleted {limit} messages", delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Deleted {limit} messages of {member.mention}", delete_after=3)

@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, user: discord.User, *, value):
  await user.send(f"**{value}**")
  await user.send(f"||Sent by {ctx.author.name}||")
  await ctx.send("DM sent!")

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, *, user: discord.User):
    if user is None:
        embed = discord.Embed(
            color=discord.Colour.orange(),
            title=f'{ctx.author.name}',
            description='Please specify the user you want to warn\n Use:`+warn @user`')
        await ctx.send(embed=embed)
    embed = discord.Embed(color=discord.Colour.orange(),
    title=f'{user.name}, you have been warned!',
    description=f'by {ctx.author.name}')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member is None:
        embed = discord.Embed(
            color=discord.Colour.orange(),
            title=f'{ctx.author.name}',
            description='Please specify the user you want to warn\n Use:`+kick @user`')
        await ctx.send(embed=embed)
    await member.kick(reason=reason)
    embed = discord.Embed(color=discord.Colour.orange(),
    title=f'Goodbye, {member.name}',
    description=f'kicked by {ctx.author.name}')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member is None:
        embed = discord.Embed(
            color=discord.Colour.orange(),
            title=f'{ctx.author.name}',
            description='Please specify the user you want to warn\n Use:`+ban @user`')
        await ctx.send(embed=embed)
    await member.ban(reason=reason)
    embed = discord.Embed(color=discord.Colour.orange(),
    title=f'Goodbye, {member.name}',
    description=f'banned by {ctx.author.name}')
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"Muted {member} >:D")
    else:
        await member.add_roles(role) 
        await ctx.send(f"Muted {member} >:D")
@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.remove_roles(role)
        await ctx.send(f"Unmuted {member}")
    else:
        await member.remove_roles(role) 
        await ctx.send(f"Unmuted {member}")

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
    embed = discord.Embed(title=name + "'s Information", color=discord.Color.orange())
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
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await asyncio.sleep(1)
    await ctx.message.delete()
    await ctx.send('Connected!', delete_after=3)
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await asyncio.sleep(1)
    await ctx.message.delete()
    await ctx.send('Disconnected!', delete_after=3)
@bot.command()
async def voicemute(ctx): #???
    voice_client = ctx.guild.voice_client
    if not voice_client:
        return
    channel = voice_client.channel
    await voice_client.main_ws.voice_state(ctx.guild.id, channel.id, self_mute=True)
    await ctx.send('Muted!', delete_after=3)

@bot.command(aliases=['calc'])
async def calculate(ctx, *, q):
    await ctx.send(f"{q}={eval(q)}")

@bot.command(aliases=['pick'])
async def choose(ctx, *, choices: str):
    await ctx.send('I choose: ``{}``'.format(random.choice(choices.split("|"))))

@bot.command()
async def regional(ctx, *, msg):
    await ctx.message.delete()
    msg = list(msg)
    regional_list = [bot.regionals[x.lower()] if x.isalnum() or x in ["!", "?"] else x for x in msg]
    regional_output = '\u200b'.join(regional_list)
    await ctx.send(regional_output)

@bot.command(aliases=['roll'])
async def dice(ctx):
  dice6=["1","2","3","4","5","6"]
  msg = await ctx.send("Rolling the dice~")
  await asyncio.sleep(3)
  await msg.delete()
  await ctx.send(f"It landed on {random.choice(dice6)}!")

@bot.command(aliases=['flip'])
async def coin(ctx):
  coin2=["head","tail"]
  childe=["Well, I'd choose head though...","Well, I'd choose tail though...","Do you believe on that?","","","","And you landed on my heart ;)"]
  msg = await ctx.send("Fliping the coin~")
  await asyncio.sleep(3)
  await msg.delete()
  await ctx.send(f"It landed on {random.choice(coin2)}. {random.choice(childe)}")

@bot.command(aliases=['8ball'])
async def ball8(ctx, *, msg: str):
        await ctx.send("Let ~~my~~ **8**ball decide your fate ;D")
        answer = random.randint(0, 19)
        em = discord.Embed(color=discord.Colour.orange())
        em.add_field(name='\u2753 Question', value=msg)
        em.add_field(name='\ud83c\udfb1 8ball', value=bot.ball[answer], inline=False)
        await ctx.send(content=None, embed=em)
        await ctx.message.delete()

@bot.command()
async def servers(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        await ctx.send("__**Childe's active servers:**__")
        activeservers = bot.guilds
        for guild in activeservers:
            await ctx.send(f'Server name:`{guild.name}`,\nServer ID:`{guild.id}`,\nServer Owner:`{guild.owner}`\n ––––––––––––––––––––––––––––––')

@bot.command()
async def say(ctx, *, msg):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.message.delete()
    await ctx.send(msg)

@tasks.loop(minutes=5)
async def presence_change():
    await asyncio.sleep(10)
    await bot.change_presence(activity=choice(presence))
    channel = bot.get_channel(841614719562285086)
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

bot.load_extension("cogs.general")
keep_alive()
bot.run(os.getenv('TOKEN'))