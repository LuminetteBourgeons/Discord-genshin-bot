# WORK IN PROGRESS
# Requestan Septo :)

# Development stopped

import discord
from discord.ext import commands
# from keep_alive import keep_alive
import os

bot = commands.Bot("tao!")

Hu_tao= ['Hu Tao', 'Hu tao', 'hu tao', 'Hutao', 'hutao']

game = discord.Game("WhO TaO??")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    if any(word in message.content for word in Hu_tao):
        await message.channel.send('Wangy wangy~ :heart:')
        await bot.process_commands(message)

# keep_alive()
bot.run(os.getenv('TOKEN'))
