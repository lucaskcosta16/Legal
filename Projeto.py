import discord
import random
import asyncio
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')
    
resp = 0
tent = 0

@bot.command()
async def guess(ctx):
    resp = random.randint(1,100)
    tent = 5
    await ctx.send("Adivinhe um número entre 1 e 100. Você tem 5 tentativas!")
    
    def check(m):
        return m.author == ctx.author and m.content.isdigit()

    for i in range(tent):
        msg = await bot.wait_for("message", check=check)

        chute = int(msg.content)

        if chute == resp:
            await ctx.send(f"Você Acertou!!!")
            return
        elif chute <= resp:
            await ctx.send(f'O número é MAIOR! (Tentativas restantes: {tent - i - 1})')
        else:
            await ctx.send(f'O número é MENOR! (Tentativas restantes: {tent - i - 1})')

    await ctx.send(f'Suas tentativas acabaram! O número era {resp}.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

bot.run("O discord troca o meu token se eu botar ele aqui ent bota o seu quando for testar")
