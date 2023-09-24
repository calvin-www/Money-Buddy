import discord
from discord.ext import commands
import asyncio
from .vars import *
from discord import ui

class Edit(commands.Cog):
    def __init__(self,client):
        self.client = client

    #edit an existing category or expense
    @commands.command(name="edit", brief="- edit an exisiting category or expense")
    async def edit(self, ctx, *args:str):       
        #return format help if no arguments given
        if len(args) == 0:
            await ctx.send("```edit [category]``` or ```edit [category] [expense number]```")
        #only 1 argument given: category is edited
        elif len(args) == 1:
            cat = args[0]
            #check if category asked is a valid category
            if cat not in expenses[ctx.author.id]:
                await ctx.send("Sorry that category doesn't seem to exist :(")
            #prompt the user what to edit the category to
            else:
                new_catagory =  await prompt1(self.client,ctx,'what would you like to change ' + cat + ' to?',timeout=20)
                expenses[ctx.author.id][new_catagory] = expenses[ctx.author.id].pop(cat)
                await ctx.send('Successfully changed ' + cat + ' to '+ new_catagory+'!')
                update_db()
        #if 2 arguments passed: 1st argument defines the category, 2nd argument defines the expense
        elif len(args) == 2:
            args = list(args)
            cat = args[0]
            #check if category requested is valid
            if cat not in expenses[ctx.author.id]:
                await ctx.send("Sorry that category doesn't seem to exist :(")
            #check if expense requested is within the list of expenses
            elif int(args[1]) > len(expenses[ctx.author.id][cat]):
                print('a')
                await ctx.send('please pick a number that exists within the category :)')
            #prompt the user on what to change the expense to
            else:
                new_expense = await prompt2(self.client,ctx,'what would you like to change ' + str(expenses[ctx.author.id][str(args[0])][int(args[1]) - 1]) + ' to?', timeout=20 )
                expenses[ctx.author.id][args[0]][int(args[1]) - 1] = new_expense
                update_db()
                await ctx.send("Successfully changed to " + str(new_expense)+ '!')
        else:
            #format help if no arguments are passed
            await ctx.send('please format yor edit request as edit [category] or edit [category] [# of expense]')

#helper function to ask user what new category should be named
async def prompt1(client, ctx, message: str, timeout: int):
    await ctx.send(message)
    message = await client.wait_for('message', check = lambda message: message.author == ctx.author,timeout=timeout)
    return message.content

#helper function to ask user what new expense is
async def prompt2(client, ctx, message: str, timeout: int):
    await ctx.send(message)
    message = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=timeout)
    args = message.content.split()
    #check if new expense input is valid
    try:
        args[1]=float(args[1])
    except Exception as e:
        args[1]=0
    
    if args[1] <= 0.0:
        ctx.send("Try again. The amount is invalid")
        return None
    return args



async def setup(client):
    await client.add_cog(Edit(client))