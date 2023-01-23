import discord

from src.API import GET, Embed
from discord.ext import commands
from src.WILD import Level as Wild

import svgwrite
from cairosvg import svg2png
from io import BytesIO

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)
client = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot ready')

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

@bot.slash_command(name='level', description='Узнать свой уровень')
async def __levelinfo(ctx):
    dwg = svgwrite.Drawing("rectangle_rounded.svg", (600, 180))
    dwg.embed_font("Rubik Medium", "fonts\Rubik-Medium.ttf")
    dwg.embed_font("Rubik Light", "fonts\Rubik-Light.ttf")
    dwg.embed_font("Rubik Regular", "fonts\Rubik-Regular.ttf")
    dwg.embed_font("Rubik Bold", "fonts\Rubik-Bold.ttf")
    dwg.add(dwg.rect((0, 0), (600, 180), rx=0, ry=0, fill=svgwrite.rgb(54, 57, 63), opacity=1))
    dwg.add(dwg.rect((180, 74), (400, 30), rx=0, ry=0, fill=svgwrite.rgb(0, 0, 0), opacity=0.25))
    dwg.add(dwg.rect((180, 128), (400, 10), rx=5, ry=5, fill=svgwrite.rgb(0, 0, 0), opacity=0.25))
    dwg.add(dwg.rect((180, 128), (173, 10), rx=5, ry=5, fill=svgwrite.rgb(255, 255, 255), opacity=1))
    dwg.add(dwg.image(ctx.author.avatar.url, insert=(20, 20), size=(140, 140)))
    # print(ctx.author.avatar.url)
    dwg.add(dwg.text('Elaskor, что ты тут хочешь увидеть ?', (180, 46), font_size=16, font_family="Rubik Medium", fill="white"))
    dwg.add(dwg.text('Вы уже с нами 234 дня, не маленький срок !', (180, 58), font_size=12, font_family="Rubik Light", fill="white"))
    dwg.add(dwg.text('Ну а присоединились вы к нам 21.03.19', (180, 68), font_size=10, font_family="Rubik Light", fill="white", opacity=0.5))
    dwg.add(dwg.text('Пользователь • 344 Опыта', (180, 123), font_size=14, font_family="Rubik Bold", fill="white", opacity=1))
    dwg.add(dwg.text('Уровень 4', (180, 153), font_size=10, font_family="Rubik Regular", fill="white", opacity=1))
    dwg.add(dwg.text('Уровень 5', (529, 153), font_size=10, font_family="Rubik Regular", fill="white", opacity=1))
    dwg.add(dwg.text('22:57', (529, 45), font_size=18, font_family="Rubik Bold", fill="white", opacity=1))
    dwg.add(dwg.text('Вс, 21 июня', (542, 52), font_size=7, font_family="Rubik Light", fill="white", opacity=1))
    dwg.add(dwg.text('Достижения', (487, 68), font_size=14, font_family="Rubik Medium", fill="white", opacity=1))
    res = BytesIO()
    svg2png(bytestring=dwg.tostring(), write_to=res, dpi=300, scale=4)
    res.seek(0)
    await ctx.respond(file=discord.File(res, 'by Apier#4141.png'))

bot.run('MTA1NTQwMjMyNjU4MTU3NTcwMA.GfzwZD.AblMjeWBxMUAwIqy1wOaThvwoStm_XUqSq7BXg')
