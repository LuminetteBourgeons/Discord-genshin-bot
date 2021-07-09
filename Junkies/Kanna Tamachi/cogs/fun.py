import discord
from discord.ext import commands
import random, asyncio

orange=0xe68a89

class Fun(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command(aliases=['roll'])
  async def dice(self, ctx):
    dice6=["1","2","3","4","5","6"]
    await ctx.send("Rolling the dice~", delete_after=3)
    await asyncio.sleep(3)
    embed = discord.Embed(title=f"Rolled a dice! 🎲", description=f"It landed on {random.choice(dice6)}!",colour=orange)
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['flip'])
  async def coin(self, ctx):
    coin2=["head","tail"]
    childe=[
      "Well, I'd choose head though...",
      "Well, I'd choose tail though...",
      "Do you believe on that?",
      "",
      "",
      "",
      "And you landed on my heart ;)"
      ]
    await ctx.send("Flipping the coin~", delete_after=3)
    await asyncio.sleep(3)
    embed = discord.Embed(title=f"Flipped a coin! 🪙", description=f"It landed on {random.choice(coin2)}. {random.choice(childe)}",colour=orange)
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Fun(bot))