import random
import discord
import colorama

with open("token", "r") as file:
    TOKEN=file.read()

def random_event():
    gen=random.randint(68,69)
    print(gen)
    if gen==69:
        with open("stats", "r") as file:
            LATEST_STATS=file.read()
        LATEST_STATS=int(LATEST_STATS)
        LATEST_STATS=LATEST_STATS+1
        with open("stats", "w") as file:
            file.write(str(LATEST_STATS))
        return "IM HUNGY"
    else:
        return "LUCKY BASTARD"

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Bot is running [{bot.user}]")

@bot.event
async def on_message(msg):
    CHANNEL=msg.channel
    print(CHANNEL)
    if msg.author.bot:
        pass
    else:
        if str(CHANNEL) == "no-eating":
            return
        else:
            message = random_event()
            if message == "LUCKY BASTARD":
                pass
            else:
                embed = discord.Embed(title="MESSAGE EATEN :hamburger: :french_fries: :pizza:",
                                      description="Caseoh ate your message! :hamburger: :french_fries: :pizza:",
                                      color=0x992d22)
                print(msg.channel)
                if "Direct Message" in str(msg.channel):
                    pass
                elif "Direct Message" not in str(msg.channel):
                    await msg.delete()
                    await msg.channel.send(embed=embed)

@bot.command(description="Track the amount of messages eaten by caseoh")
async def stats(msg):
    with open("stats", "r") as file:
        STATS=file.read()
        if STATS=="0":
            embed = discord.Embed(title="CaseOh Stats", description=f"Case hasn't eaten any messages yet.", color=0x992d22)
        else:
            embed = discord.Embed(title="CaseOh Stats", description=f"Case already ate {STATS} messages.", color=0x992d22)
    await msg.respond(embed=embed)

bot.run(TOKEN)