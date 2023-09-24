import io
import discord
from discord.ext import commands
import asyncio
from .vars import *
from discord import ui
import csv

class Export(commands.Cog):
  def __init__(self,client):
      self.client = client
  
  @commands.command(name="save")
  async def save(self, ctx: commands.Context):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    #writer = csv.writer(file)
    writer.writerow(["S/N", "Date", "Category", "Amount", "Description"])
    count=1
    for category, exps in expenses[ctx.author.id].items():
      for exp in exps:
        writer.writerow([count, exp[0], category, exp[1], exp[2]])
        count+=1
    buffer.seek(0)
    await ctx.send(file=discord.File(buffer, 'expense.csv'))

    



async def setup(client):
  await client.add_cog(Export(client))