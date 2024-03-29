import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
async def on_ready(ctx):
     await ctx.send("Напишите '$info' чтобы  вывести это сообщение.\nНапишите '$garbage' чтобы увидеть сколько разлагаеться мусор.\nНапишите '$links' чтоб увидеть полезные ссылки по теме загрязнения планеты.")
   
@bot.command()
async def garbage(ctx):
    for image in os.listdir('images'):
        with open(f'images/{image}', 'rb') as file:
            discord_image = discord.File(file)
            await ctx.send(file=discord_image)

@bot.command()
async def links(ctx):
    await ctx.send("https://www.pinterest.com/ooooooooooo9889/из-мусора/")

@bot.command()
async def info(ctx):
    await ctx.send("Напишите '$info' чтобы  вывести это сообщение.\nНапишите '$garbage' чтобы увидеть сколько разлагаеться мусор.\nНапишите '$links' чтоб увидеть полезные ссылки по теме загрязнения планеты.")



bot.run('TOKEN')
