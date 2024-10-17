from discord.ext import commands
import discord
import datetime
import pytz
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = 1239732804309352478

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event #starts the bot
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    embed = discord.Embed(title='Gacha Tracker', description='Hello! Welcome to the Gacha Tracker Bot!\n\nThis is a bot used to track the reset times of different gacha games.\n\nTo get started, type !info')
    await channel.send(embed=embed)

@bot.command() #info command
async def info(ctx):
    embed = discord.Embed(title='Info', description="!info = shows the list of available commands\n!all = shows a list of all games\n!search <game> = shows all of the reset times of the specified game")
    await ctx.send(embed=embed)

@bot.command() #all command
async def all(ctx):
    embed = discord.Embed(title='All Games', description="Genshin Impact\nHonkai: Star Rail\nArknights\nNikke\nFate/Grand Order\nWuthering Waves\nAzur Lane\nPrincess Connect: Re:Dive\nGranblue Fantasy\nAFK Journey")
    await ctx.send(embed=embed)

timezone = pytz.timezone('America/New_York')
now = datetime.datetime.now(timezone)

#Genshin Impact / Honkai Star Rail / Wuthering Waves Daily Reset
GID_reset_time = now.replace(hour=5, minute=0, second=0)
GID_time_difference = GID_reset_time - now
if GID_time_difference < datetime.timedelta(0):
    GID_time_difference += datetime.timedelta(days=1)

#Genshin Impact / Honkai Star Rail / Wuthering Waves Weekly Reset
GIW_reset_time = now.replace(hour=5, minute=0, second=0) + datetime.timedelta(days=8-now.isoweekday())
GIW_time_difference = GIW_reset_time - now

#Arknights Daily Reset
AKD_reset_time = now.replace(hour=7, minute=0, second=0)
AKD_time_difference = AKD_reset_time - now
if AKD_time_difference < datetime.timedelta(0):
    AKD_time_difference += datetime.timedelta(days=1)

#Arknights Weekly Reset
AKW_reset_time = now.replace(hour=7, minute=0, second=0) + datetime.timedelta(days=8-now.isoweekday())
AKW_time_difference = AKW_reset_time - now

#Nikke Daily Reset
NKD_reset_time = now.replace(hour=16, minute=0, second=0)
NKD_time_difference = NKD_reset_time - now
if NKD_time_difference < datetime.timedelta(0):
    NKD_time_difference += datetime.timedelta(days=1)

#FGO Daily Reset
FGOD_reset_time = now.replace(hour=0, minute=0, second=0)
FGOD_time_difference = FGOD_reset_time - now
if FGOD_time_difference < datetime.timedelta(0):
    FGOD_time_difference += datetime.timedelta(days=1)

#FGO Weekly Reset
FGOW_reset_time = now.replace(hour=20, minute=0, second=0) + datetime.timedelta(days=7-now.isoweekday())
FGOW_time_difference = FGOW_reset_time - now

#Azur Lane Daily Reset
ALD_reset_time = now.replace(hour=3, minute=0, second=0)
ALD_time_difference = ALD_reset_time - now
if ALD_time_difference < datetime.timedelta(0):
    ALD_time_difference += datetime.timedelta(days=1)

#Azur Lane Weekly Reset
ALW_reset_time = now.replace(hour=3, minute=0, second=0) + datetime.timedelta(days=8-now.isoweekday())
ALW_time_difference = ALW_reset_time - now

#Priconne Lane Weekly Reset
PCW_reset_time = now.replace(hour=16, minute=0, second=0) + datetime.timedelta(days=7-now.isoweekday())
PCW_time_difference = PCW_reset_time - now

#AFKJ Daily Reset
AJD_reset_time = now.replace(hour=20, minute=0, second=0)
AJD_time_difference = AJD_reset_time - now
if AJD_time_difference < datetime.timedelta(0):
    AJD_time_difference += datetime.timedelta(days=1)

#AFKJ Weekly Reset
AJW_reset_time = now.replace(hour=20, minute=0, second=0) + datetime.timedelta(days=7-now.isoweekday())
AJW_time_difference = AJW_reset_time - now



game_info = { #dictionary of games and their reset times
    "Genshin Impact": "NA Daily Reset will be in: " + str(GID_time_difference) + "\nNA Weekly Reset will be in: " + str(GIW_time_difference),
    "Honkai: Star Rail": "NA Daily Reset will be in: " + str(GID_time_difference) + "\nNA Weekly Reset will be in: " + str(GIW_time_difference),
    "Arknights": "Daily Reset will be in: " + str(AKD_time_difference) + "\nWeekly Reset will be in: " + str(AKW_time_difference),
    "Nikke": "Daily Reset will be in: " + str(NKD_time_difference),
    "Fate/Grand Order": "Daily Reset will be in: " + str(FGOD_time_difference) + "\nWeekly Reset will be in: " + str(FGOW_time_difference),
    "Wuthering Waves": "NA Daily Reset will be in: " + str(GID_time_difference) + "\nNA Weekly Reset will be in: " + str(GIW_time_difference),
    "Azur Lane": "Daily Reset will be in: " + str(ALD_time_difference) + "\nWeekly Reset will be in: " + str(ALW_time_difference),
    "Princess Connect: Re:Dive": "JP Daily Reset will be in: " + str(NKD_time_difference) + "\nJP Weekly Reset will be in: " + str(PCW_time_difference),
    "Granblue Fantasy": "Daily Reset will be in: " + str(NKD_time_difference) + "\nWeekly Reset will be in: " + str(PCW_time_difference),
    "AFK Journey": "Daily Reset will be in: " + str(AJD_time_difference) + "\nWeekly Reset will be in: " + str(AJW_time_difference)
}

@bot.command() #search command
async def search(ctx, *, game):
    if game in game_info:
        embed = discord.Embed(title=game)
        embed.add_field(name='', value=game_info[game], inline = False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Game not found")
        await ctx.send(embed=embed)

bot.run(BOT_TOKEN)
