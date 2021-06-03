import discord
from discord.ext import commands
import googletrans
from googletrans import Translator
import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json")as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)
token = configData["Token"]
client= commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("bot is online")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"translating for {len(client.guilds)} servers | !help"))

@client.command(aliases = ["trans"])
async def translate(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    #you can switch embed out to just a regular ctx.send(a.text)
    em = discord.Embed (title = f"translator to {lang}" , description = (a.text), color = discord.Color.orange())
    
    await ctx.send(embed = em)


client.run(token)