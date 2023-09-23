import discord
from discord.ext import commands
import asyncio


class category_select(commands.cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name = 'ping')
    async def ping(ctx):
        await ctx.send("pong")

async def setup(client):
    await client.add_cog(category_select(client))
    