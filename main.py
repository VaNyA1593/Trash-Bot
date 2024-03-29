import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def мусор(ctx):
    for image in os.listdir('images'):
        with open(f'images/{image}', 'rb') as file:
            discord_image = discord.File(file)
            await ctx.send(file=discord_image)


bot.run('TOKEN')
