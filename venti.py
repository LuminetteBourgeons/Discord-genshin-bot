# WORK IN PROGRESS
# Didedikasikan untuk Discord server Rumah Mine
# Masih dikembangkan biar Mine makin halu.

import discord
from discord.ext import commands
import os
import random
# from keep_alive import keep_alive

client = discord.Client()

bot = commands.Bot(';;')

curse_words = ["fuck", "Fuck", "FUCK", "Shit", "SHIT", "shit", "Piss", "piss", "Dick", "dick", "asshole", "Asshole", "ASSHOLE", "Bitch", "bitch", "Cunt", "cunt", "Anjing", "anjing", "bangsat","Bangsat", "ngentot", "Ngentot", "peepee", "poopoo", "pussy", "Pussy", "damn", "DAMN", "Damn"]
# you curse you die


starter_shut = [
  "Language",
  "You wanna get fucked?",
  "Hey, watch it."
]


game = discord.Game("with Mine")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=game)
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(';;hi'):
        await message.channel.send('Shut the fuck up')

    if message.content.startswith(';;Hi'):
        await message.channel.send('Shut the fuck up')

    if message.content.startswith(';;hello'):
        await message.channel.send('hi.')

    if message.content.startswith(';;Hello'):
        await message.channel.send('hi.')
    
    if message.content.startswith(';;Diluc'):
        await message.channel.send('R E T R I B U T I O N ! !')
        
    if message.content.startswith(';;diluc'):
        await message.channel.send('R E T R I B U T I O N ! !')
    
    if message.content.startswith(';;I love u'):
        await message.channel.send('thanks')
    
    if any(word in message.content for word in curse_words):
       await message.channel.send(random.choice(starter_shut))
    
# keep_alive ()
client.run(os.getenv('TOKEN'))
