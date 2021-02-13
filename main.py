import os
from dotenv import load_dotenv
from discord.ext import commands
import time
from discord import message
import json
import urllib.request
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
@bot.command(name = 'suma')
async def sumar(ctx, num1, num2):

  response = int(num1)+int(num2)
  await ctx.send(response)
@bot.command(name = 'hazlosdeberes')
async def deberes(ctx):
  await ctx.send("Lo siento amigo pero tienes que esforzarte :) te servira para el futuro")

@bot.command(name = 'hora')
async def hora(ctx):
  await ctx.send(time.strftime("%H:%M:%S"))

@bot.command(name = 'boty')
async def boty(ctx):
  await ctx.send('''hola soy boty un bot muy refachero creado por Alerty y se hacer cosas raras como:
  !suma numero numero
  (sumar dos numeros)
  !hazlosdeberes
  (descubrelo :) )
  !hora
  (da la hora)
  !memes
  envía memes
  !malo
  !boty
  para saber más información''')

@bot.command(name = 'memes')
async def memes(ctx):
  await ctx.send('https://tenor.com/view/shrek-shreck-gif-18286039')
  await ctx.send('https://tenor.com/view/rdj-yeah-sure-rolleyes-iron-man-gif-10063629')
  await ctx.send('https://tenor.com/view/kid-funny-dance-dancing-gif-13442955')
  await ctx.send('https://tenor.com/view/cat-whats-happening-im-not-hungry-gif-14868925')
  await ctx.send('https://tenor.com/view/laughing-big-mouth-eat-screaming-crazy-gif-12904194')
  await ctx.send('https://tenor.com/view/perro-chistoso-pug-gif-8630144')

@bot.command(name='malo')
async def memes(ctx):
  await ctx.send('https://sd.keepcalm-o-matic.co.uk/i/que-dijiste-3.png')
  await ctx.send('¿¿¿¿queee haaas dichooo????')

@bot.command(name='rank')
async def rank(ctx):
    await ctx.send('no hay que ser tan competitivo ¿que te importa tu rango?')
    await ctx.send('https://www.bing.com/images/search?view=detailV2&ccid=Wg7aOzfC&id=CD4500C7F0D7E32F1A5E69DDDD4B787C72B60087&thid=OIP.Wg7aOzfC4Vi68k50fbFDYQHaEK&mediaurl=https%3a%2f%2fsto')

@bot.command(name='hola')
async def hola(ctx):
    await ctx.send('Yo te quiero saludar también ¡hooolaaaa! soy boty pon !boty para saber más sobre mi')

@bot.command(name='stop')
async def stop(ctx):
    await ctx.send('<stop') 
time.strftime("%H:%M:%S")
bot.run(TOKEN)
