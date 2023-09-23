import discord
from discord.ext import commands
import asyncio
from .vars import *
from discord import ui

class categories(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(name="categories")
    async def categories(self, ctx: commands.Context,):
        await ctx.send('Your categories are:')
        await ctx.send(" ".join(expenses))
    



async def setup(client):
    await client.add_cog(categories(client))