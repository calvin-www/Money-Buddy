import discord
from discord.ext import commands
import asyncio
from .vars import *
from discord import ui

#add a category
async def addCategory(ctx: commands.Context, args: list):
    expenses[ctx.author.id][args[0]]=[]
    update_db()
    return await ctx.channel.send(f"You have successfully added the {args[0]} category!")

# cogs let you put related commands and functions together under a class
class Add(commands.Cog):

    def __init__(self, client):
        self.client = client

    #adds a category or expense
    @commands.command(name='add',brief="- adds a new category or expense")
    async def add(self, ctx: commands.Context, *args: str):
        #add arg0 arg1 arg2 arg3 : where arg0 is a category and arg1-3 is an expense
        args = list(args)
        #check if the arguments are 1, as that would be the desired name of a category
        if len(args) == 1:
            #check if arg0 already exists
            if args[0] in expenses[ctx.author.id]:
                return await ctx.channel.send(f"{args[0]} is already a category!")
            #add new category
            return await addCategory(ctx, args)
        
        if len(args) >= 3:
            desc = ""
            #assumes the extra arguments are meant to be multi worded titles
            if len(args)>=4:
                desc = " ".join(args[3:])
            #add new category if it doesn't exist
            if args[0] not in expenses[ctx.author.id]:
                await addCategory(ctx, args)
            #if everything matches, expense alr exists
            if [args[1], args[2], desc] in expenses[ctx.author.id][args[0]]:
                return await ctx.send("Sorry, you added that expense previously")
            
            try:
                #test if values are in the right place or right range
                args[2]=float(args[2])
            except Exception as e:
                args[2]=0
            if args[2] <= 0.0 or args[2]==None:
                return await ctx.send("Sorry, please input the expense in this format:```add [category] [date(mm/dd/yy)] [amount spent(no $)] [title]``` ")
            #add the new expense to the list of expenses
            expenses[ctx.author.id][args[0]].append([args[1], float(args[2]), desc])
            update_db()
            return await ctx.channel.send("Success!")   
        #return format help if no arguments given
        return await ctx.send("```add [category]``` or ```add [category] [date(mm/dd/yy)] [amount spent(no $)] [title]```")

       
async def setup(client):
    await client.add_cog(Add(client))
