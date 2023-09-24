import discord
from discord.ext import commands
import asyncio
from .vars import *
from discord import ui

async def addCategory(ctx: commands.Context, args: list):
    expenses[ctx.author.id][args[0]]=[]
    print(type(ctx.author.id))
    update_db()
    print(expenses)
    return await ctx.channel.send(f"You have successfully added the {args[0]} category")

# cogs let you put related commands and functions together under a class
class AddExpense(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='add')
    async def add(self, ctx: commands.Context, *args: str):
        args = list(args)
        
        if len(args) == 1:
            if args[0] in expenses[ctx.author.id]:
                return await ctx.channel.send(f"{args[0]} is already a category")
            return await addCategory(ctx, args)
        
        if len(args) >= 3:
            desc = ""
            if len(args)>=4:
                desc = " ".join(args[3:])
            if args[0] not in expenses[ctx.author.id]:
                await addCategory(ctx, args)
            if [args[1], args[2], desc] in expenses[ctx.author.id][args[0]]:
                return await ctx.send("Sorry, you added that expense previously")
            
            try:
                args[2]=float(args[2])
            except Exception as e:
                args[2]=0
            
            if args[2] <= 0.0 or args[2]==None:
                return await ctx.send("Try again. The amount has to be just a number.")
            expenses[ctx.author.id][args[0]].append([args[1], float(args[2]), desc])
            update_db()
            return await ctx.send(f"New {args[0]} expense added!")
            #self.bot.get_command('play'),
            #return await ctx.invoke(self.client.get_command('view'), query=''+args[0])
        return await ctx.channel.send("You have to add in one of these formats\n1. add category\n2. add category date amount decsription(optional)")
       

    


# add this cog to the client
async def setup(client):
    await client.add_cog(AddExpense(client))
