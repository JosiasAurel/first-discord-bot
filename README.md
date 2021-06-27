# My First Discord Bot

This is my first discord bot created as a way of learning how to manipulate discord API in Python and creating a bot.

## How to use

clone the repository

```shell
https://github.com/JosiasAurel/first-discord-bot.git
```

Install dependencies

```shell
pip install -r requirements.txt
```

Create a new app in discord developer console. Then create a bot.
Create a `.env` file and add the Discord API token for your bot.
Also add the guild name in which your bot will be leaving

You `.env` file should look like this :

```env
DISCORD_TOKEN=<your-token>
DISCORD_GUILD=<server-or-guild-name>
```

Run the `main.py` file with `python` if you are on windows or `python3` on UNIX variants like Mac and Linux.

```shell
python main.py
```

Go to your channel and type `!help` to view available commands
