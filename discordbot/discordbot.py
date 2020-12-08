# Ohjelma on Discord alustalla toimiva botti
# Sen avulla voi eri komennoilla suorittaa toimia Discord palvelimella

# Importit
import discord
from discord.ext import commands
import credentials
import ominaisuudet

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def makaronilaatikko(ctx):
    await ctx.send(ominaisuudet.makaronilaatikko_resepti())

@bot.command()
async def youtube(ctx, *, arg):
    await ctx.send(ominaisuudet.youtube_search(arg))

bot.run(credentials.TOKEN)