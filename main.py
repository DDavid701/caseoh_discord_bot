import random
import discord
import colorama
from dotenv import load_dotenv
import os
colorama.init(autoreset=True)
load_dotenv("options.ENV")
TOKEN_FILE=os.getenv("TokenFile")
STATS_FILE=os.getenv("StatsFile")
CONFIG_FOLDER=os.getenv("ConfigFolder")
FROM=os.getenv("FROM")
TO=os.getenv("TO")
TRIGGER=os.getenv("TRIGGER")
SAVE_CHANNEL=os.getenv("SAVE_CHANNEL")
load_dotenv(f'{CONFIG_FOLDER}/stats.env')
EMBED_TITLE=os.getenv("EMBED_TITLE")
COMMAND_DESCRIPTION=os.getenv("COMMAND_DESCRIPTION")
DESCRIPTION=os.getenv("DESCRIPTION")
ZERO_DESCRIPTION=os.getenv("ZERO_DESCRIPTION")
load_dotenv(f'{CONFIG_FOLDER}/on_message.env')
ONMESSAGE_TITLE=os.getenv("ONMESSAGE_TITLE")
ONMESSAGE_DESCRIPTION=os.getenv("ONMESSAGE_DESCRIPTION")
PREFIX=colorama.Fore.CYAN+"LOG "+colorama.Fore.LIGHTBLACK_EX+"× "+colorama.Fore.LIGHTWHITE_EX

print(PREFIX+"Getting Token....")
with open(TOKEN_FILE, "r") as file:
    TOKEN=file.read()
    print(PREFIX+f"The Token is '{TOKEN_FILE}'")

def LUCK():
    gen=random.randint(int(FROM),int(TO))
    if str(gen)==str(TRIGGER):
        with open(STATS_FILE, "r") as file:
            LATEST_STATS=file.read()
        LATEST_STATS=int(LATEST_STATS)+1
        with open(STATS_FILE, "w") as file:
            file.write(str(LATEST_STATS))
        return 0
    else:
        return 1

bot = discord.Bot()

@bot.event
async def on_ready():
    print(PREFIX+f"Bot is running [{bot.user}]")

@bot.event
async def on_message(msg):
    CHANNEL=str(msg.channel)
    if msg.author.bot:
        pass
    else:
        if str(CHANNEL)==SAVE_CHANNEL:
            return
        else:
            CHANCE=LUCK()
            if CHANCE==1:
                pass
            else:
                embed = discord.Embed(title=ONMESSAGE_TITLE,
                                      description=ONMESSAGE_DESCRIPTION,
                                      color=0x992d22)
                if "Direct Message" in CHANNEL:
                    pass
                elif "Direct Message" not in CHANNEL:
                    await msg.delete()
                    await msg.channel.send(embed=embed)
                else:
                    pass

@bot.command(description=COMMAND_DESCRIPTION)
async def stats(msg):
    with open(STATS_FILE, "r") as file:
        STATS=file.read()
        if STATS=="0":
            embed = discord.Embed(title=EMBED_TITLE, description=ZERO_DESCRIPTION, color=0x992d22)
        else:
            if "%STATS%" in DESCRIPTION:
                DESCRIPTION_NEW=DESCRIPTION.replace("%STATS%", f"{STATS}")
            embed = discord.Embed(title=EMBED_TITLE, description=DESCRIPTION_NEW, color=0x992d22)
    await msg.respond(embed=embed)

bot.run(TOKEN)