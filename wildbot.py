import discord

from src.API import GET, Embed
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)
client = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot ready ✅')

@bot.event
async def on_member_join(member):
    getWelocme = await GET.Channel.getByName(bot, 'welcome')
    if getWelocme is None:
        print('None')
    else: await Embed.Embed.joinMessage(member, getWelocme)

@bot.event  
async def on_member_remove(member):
    getWelocme = await GET.Channel.getByName(bot, 'welcome')
    if getWelocme is None:
        print('None')
    else: await Embed.Embed.removeMessage(member, getWelocme)

bot.run('MTA1NTQwMjMyNjU4MTU3NTcwMA.GpUTQr.ZNbBjNhEJQznVwyCxfb7jRDmgmT3VukheQ9_vs')