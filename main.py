
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

# command to create channel


@bot.command(name="createChannel" help="Creates a new channel. Takes a name e.g createChannel test")
@commands.has_role("admin")  # check if is admin
async def create_channel_handler(ctx, channel_name: str):
    curr_guild = ctx.guild
    is_existing_channel = discord.utils.find(
        lambda c: c.name == channel_name, curr_guild.channels)
    if not is_existing_channel:
        await curr_guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
    # if the error is of type check failure -> role
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You do not have permission to create a channel. You have to be Admin")

bot.run(token)
