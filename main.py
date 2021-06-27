
import discord
import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

bot = discord.Client()  # instance a new client


@bot.event
async def on_ready():  # event client has established connection with discord API
    # guild = discord.utils.find(lambda g: g.name == my_guild, bot.guilds)
    guild = discord.utils.get(bot.guilds, name=my_guild)  # get guild via name
    print(f"{bot.user} is in guild {guild.name} ID: {guild.id} ")
    members = "\n - ".join([member.name for member in guild.members])
    print("Guild Members")
    print(f'- {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f" Hi, {member.name}, Welcome to this discord server ")

bot.run(token)
