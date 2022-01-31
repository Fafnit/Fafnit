import discord 
from discord.ext import commands
import random 

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '.', case_Insensitive = True)

@client.event
async def on_ready():
  print('to on') .format(client)

@client.command()
async def menu(ctx):
 await ctx.send(f'opa {ctx.author} este e o menu :3')

@client.command()
async def opa(ctx):
 await ctx.send(f'opa {ctx.author}')

@client.event
async def on_member_join(members):
  canalboasvindas = client.get_channel(924006642520055840)
  regras = client.get_channel(924025375334494298)
  mensagem = await canalboasvindas.send(f'<:albedo1:924390011217002516> bem-vindo {member,mention}! leia as regras em {regras.mention}')

@client.command()
async def albedo(ctx):
 await ctx.send(f'fala viado')

@client.command()
async def criador(ctx):
 await ctx.send(f'meu criador é esse lindo aqui: kaileS2#5716 ;3')

client.run('OTM0MTc0NDIzNTcxOTEwNzc3.YesPug.hnsGNoLxXGwRni2uCdAAi7AvuWk')
