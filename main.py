
import discord
import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

bot = discord.Client()  # instance a new client


@bot.event
async def on_ready():  # event client has established connection with discord API
    for guild in bot.guilds:
        if guild.name == my_guild:
            break

    print(f"{bot.user} is in guild {guild.name} ID: {guild.id} ")
    members = "\n - ".join([member.name for member in guild.members])
    print("Guild Members")
    print(f'- {members}')

bot.run(token)
