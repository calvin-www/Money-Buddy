import discord
from discord.ext import commands
import asyncio
from .vars import *
from discord import ui

# cogs let you put related commands and functions together under a class
class AddExpense(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='add')
    async def add(self, ctx: commands.Context, *args: str):
        args = list(args)
        print(args)
        
        if len(args) == 1:
            if args[0] in expenses:
                return await ctx.channel.send(f"{args[0]} is already a category")
            expenses[args[0]]={}
            return await ctx.channel.send(f"You have successfully added the {args[0]} category")
        else:
            return await ctx.channel.send("You have to add in one of these formats\n1. add category\n2. add category date amount decsription(optional)")
        await ctx.channel.send(f'The count is {count[0]}')
        


# add this cog to the client
async def setup(client):
    await client.add_cog(AddExpense(client))
