import discord

class Channel:
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    async def getByName(bot, name: str):
        for channel in bot.guilds[0].channels:
            if channel.name.endswith(name): return channel
            else: 
                for channel in bot.guilds[0].channels:
                    if channel.name.startswith(name): return channel

print("GET.py ✅")