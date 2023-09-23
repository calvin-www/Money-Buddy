import datetime
from typing import Any, Optional, Union
import discord
from discord.colour import Colour
from discord.ext import commands
import asyncio

from discord.types.embed import EmbedType
from .vars import expenses

# make an expense report
class ExpenseReport(discord.Embed):
    def __init__(self, ctx, title: str, expenses: list):
        super().__init__(title=title, color=discord.Color.teal())
        self.ctx = ctx
        self.expenses = expenses

        total = 0.0
        for choice in self.expenses:
            cost: str = '{:20,.2f}'.format(float(choice[1]))
            self.add_field(name=choice[0], value=f"${cost} - {choice[2]}", inline=False)
            total += float(choice[1])

        formatted_total = '{:20,.2f}'.format(total)
        self.add_field(name=f'TOTAL: {formatted_total}', value='')


# cogs let you put related commands and functions together under a class
class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='report')
    async def report(self, ctx: commands.Context, category: str):
        category_expenses = expenses[category]

        expense_report = ExpenseReport(ctx, category, category_expenses)
        await ctx.send(embed=expense_report)


# add this cog to the client
async def setup(client):
    await client.add_cog(Report(client))
