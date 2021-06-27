
import discord
import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables

token = os.getenv("DISCORD_TOKEN")

bot = discord.Client()  # instance a new client


@bot.event
async def on_ready():
    print(f" {bot.user} has connected to the Discord 🎉")  # make me aware ;)

bot.run(token)
