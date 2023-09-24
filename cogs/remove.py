from typing import Optional
from discord.ext import commands
import discord
import asyncio

from .vars import*

# cog
class Remove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remove(self, ctx: commands.Context, category:str | None, index: int | None):
        personal_expenses = expenses[ctx.author.id]

        if not category and not index:
            await ctx.send("```remove [category]``` or ```remove [category] [expense number]```")
            return

        if not (category in personal_expenses):
            await ctx.send(f'"{category}" is not a category')
            return

        if not index:
            await ctx.send(f'remove {category}? [y]=yes/[any]=no')

            confirmation = ""

            def confirm(msg):
                nonlocal confirmation
                confirmation = msg.content
                return msg.content != None
            
            resp = None

            try:
                resp: bool = await self.client.wait_for('message', timeout=10, check=confirm)
            except asyncio.TimeoutError:
                await ctx.send('timeout')

            # removes the category
            if resp:
                if confirmation == 'y':
                    del personal_expenses[category]
                    update_db()
                    await ctx.send(f'{category} has been removed.')
                else:
                    await ctx.send('remove cancelled')

        # removes an item
        category_expenses: list = personal_expenses[category]
        if (index - 1 < len(category_expenses)):
            expense = category_expenses.pop(index - 1)
            update_db()
            await ctx.send(f'removed {expense[2]} from {category}')
        else:
            await ctx.send(f'{index} is not an expense number in "{category}"')


# add this cog to the client
async def setup(client):
    await client.add_cog(Remove(client))
