import discord
from discord.ext import commands

# Intenções
intents = discord.Intents.default()
intents.message_content = True

# Prefixo de Comando
bot = commands.Bot(command_prefix='-', intents=intents)

# Inicialização
@bot.event
async def on_ready():
    print(f'Fizemos login com {bot.user}!')

@bot.command()
async def question(ctx, trash: int):
    kgPerBag = 6.8
    dailyKg = trash * kgPerBag
    yearlyKg = dailyKg * 365

    await ctx.send(f'Você produz, em média, {dailyKg}kg de lixo por dia! Em um ano, isso resultaria em {yearlyKg}!')


bot.run('TOKEN')