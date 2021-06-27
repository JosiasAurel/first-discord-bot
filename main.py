
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  # load environment variables

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

# bot = discord.Client()  # instance a new client

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():  # event client has established connection with discord API
    # guild = discord.utils.find(lambda g: g.name == my_guild, bot.guilds)
    guild = discord.utils.get(bot.guilds, name=my_guild)  # get guild via name
    print(f"{bot.user.name} is in guild {guild.name} ID: {guild.id} ")
    members = "\n - ".join([member.name for member in guild.members])
    print("Guild Members")
    print(f'- {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f" Hi, {member.name}, Welcome to this discord server ")


""" @bot.event
async def on_message(message):
    if message.author == bot.user:  # if the bot wrote the message, do not send special message
        return

    if message.content == "hello":
        await message.channel.send("Beep boop? i hear you bro!!")
    elif message.content == "makeException":
        raise discord.DiscordException


@bot.event
async def on_error(event, *args, **kwargs):
    with open("bot.errors", "w") as errs:
        if event == "on_message":
            errs.write(f"Unhandled error : {args[0]} ")
        else:
            pass """


@bot.command(name="hello", help="Responds with a greeting")
async def great_user(ctx):
    await ctx.send("Hello from the bot too ;)")


@bot.command(name="greet", help="Greets user with a name he passes. e.g greet John")
async def great_user(ctx, name: str):
    await ctx.send(f" Hello {name} ")

bot.run(token)
