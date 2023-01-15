import discord
from datetime import datetime as dt
from time import time

class Embed:
    def __init__(self):
        super().__init__()
    async def removeMessage(member, channel):
        embed = discord.Embed(
            title=f'Всего доброго {member.display_name}',
            color=0xaf1818,
            description=f'Аккаунт создан: <t:{int(member.created_at.timestamp())}:R>\nПрисоединился: <t:{int(member.joined_at.timestamp())}:R>\nВышел: <t:{int(time())}:R>')
        embed.set_author(
            name=f'{member.display_name} ({member.id})',
            icon_url=member.display_avatar.url)
        await channel.send(embed=embed)
    async def joinMessage(member, channel):
        embed = discord.Embed(
            title=f'Добро пожаловать {member.display_name}',
            color=0x18af31,
            description=f'Аккаунт создан: <t:{int(member.created_at.timestamp())}:R>\nПрисоединился: <t:{int(member.joined_at.timestamp())}:R>')
        embed.set_author(
            name=f'{member.display_name} ({member.id})',
            icon_url=member.display_avatar.url)
        await channel.send(embed=embed)