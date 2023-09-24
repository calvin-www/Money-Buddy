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
  
  #export the data from each user as a csv file
  @commands.command(name="export",brief="- exports the categories and expenses as a csv file")
  async def export(self, ctx: commands.Context):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    #create column titles
    writer.writerow(["S/N", "Date", "Category", "Amount", "Description"])
    count = 1
    #iterate through dictionary adding, keys and values into sheet
    for category, exps in expenses[ctx.author.id].items():
      for exp in exps:
        writer.writerow([count, exp[0], category, exp[1], exp[2]])
        count+=1
    buffer.seek(0)
    #send the file back to the user
    await ctx.send(file=discord.File(buffer, 'expense.csv'))


async def setup(client):
  await client.add_cog(Export(client))