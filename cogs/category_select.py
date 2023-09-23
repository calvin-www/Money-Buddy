from typing import Optional
import discord
from discord.ext import commands
import asyncio
from .vars import *

# a poll button that inherits from discord.ui.Button
class PollButton(discord.ui.Button):
    message = ''
    count = 0

    # constructor for this poll button.
    def __init__(self, message):
        # calls the super constructor to give the label and style of the button
        super().__init__(label=message, style=discord.ButtonStyle.primary)
        self.message = message

    # defines the behavior after a user clicks a poll button (returns user choice and increments poll)
    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's choice and increment the poll
        self.count += 1
        user1 = interaction.user
        await interaction.response.send_message(f'{user1.mention}\'s choice is {self.message}', ephemeral = True)

# poll class that inherits from the discord.ui.View, basically a container for the poll buttons
class Poll(discord.ui.View):

    # constructor for this Poll
    def __init__(self, ctx, question: str, args: list, timeout):
        # timeout is how many seconds it takes before the on_timeout function runs
        super().__init__(timeout=timeout)
        self.question = question
        self.ctx = ctx
        # creates a poll button for each choice inputted and adds them to the view
        for choice in args:
            self.add_item(PollButton(choice))

    # function runs when this view times out
    async def on_timeout(self):
        await self.ctx.send(self.question)
        # sends the votes for each choice
        for item in self.children:
            await self.ctx.send(f'{item.message}: {item.count} votes')

# cogs let you put related commands and functions together under a class
class start(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name='category select')
    async def start(self, ctx: commands.Context, categories: list):
        buttons = ['+']
        for i in buttons:
            

        await ctx.send(category)

# add this cog to the client
async def setup(client):
    await client.add_cog(start(client))