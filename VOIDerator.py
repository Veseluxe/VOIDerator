import nextcord
from nextcord.ext import commands
import random

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = "oi ", intents = intents)

@bot.command(aliases = ["hello", "hey"])
async def hi(ctx):
    await ctx.reply(random.choice(["Hello!", "'Sup", "Hello, please read the <#1036185554624196650>", "Hey, btw if you have any questions, open a ticket in <#1036194707677663252>", "Hey!", "It's great to have you here"]))

@bot.command(aliases = ["support", "kelp"])
async def complain(ctx):
  await ctx.reply("If you have any problem with the server or a specific user, open a ticket in <#1036194707677663252> so that we can quickly resolve the issue")

@bot.command(aliases = ["sewy", "suii", "suiii", "sui", "siuuu", "siuu", "goal", "sewyy", "ronaldo"])
async def siu(ctx):
    await ctx.reply(random.choice(["SIUUUUU!", "SEWY!", "Muchas gracias aficion, este es para vosotros, SIUUUUUUU!", "Cristiano Ronaldo, SIUUUUUU!"]))

@bot.command(aliases=["pong"])
async def ping(ctx):
  await ctx.reply(f"Ping took me about {round(bot.latency * 1000)}ms to respond") 

@bot.event
async def on_ready():
    print(f"\n\n{bot.user.name} - {bot.user.id} is on air")
    await bot.change_presence(status = nextcord.Status.idle, activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = "VOID"))
    print("Bot presence  is active")

if __name__ == "__main__":
    bot.run("TOKEN")
