from discord.ext import commands
import locale

from .vars import *

# expense report for a specifc category
def category_report(ctx:commands.Context, category: str):
    #check if category requested is valid
    if not category in expenses[ctx.author.id]:
        return f'"{category}" is not a category', 0
    locale.setlocale(locale.LC_ALL, '')
    report: str = f"**{category}**"
    total: float = 0
    #output the formatted category
    for idx, expense in enumerate(expenses[ctx.author.id][category]):
        report += f"\n\t{idx + 1}) {expense[0]}: {expense[2]} - {locale.currency(expense[1], grouping=True)}"
        total += expense[1]
    report += f"\n\t*TOTAL: {locale.currency(total, grouping=True)}*"
    return report, total

# generates an expense report for all categories with their expenses
def all_expenses_report(ctx:commands.Context) -> str:
    report: str = ""
    total: float = 0
    #prints all expenses under their category
    for category in expenses[ctx.author.id]:
        cat_rep = category_report(ctx, category)
        report += f"\n{cat_rep[0]}"
        total += cat_rep[1]

    report += f"\n***TOTAL: {locale.currency(total, grouping=True)}***"

    return report

#overall view command for categories and expenses
class View(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="view",
                      brief="- view all expenses, a category's expenses, or all categories")
    async def view(self, ctx: commands.Context, category: str = commands.parameter(default=None, description="(optional) category to ")):
        #if 'categories' specifically requested: show just the categories
        if category == "categories":
            await ctx.send('Your categories are:')
            await ctx.send('**' + (" | ".join(expenses[ctx.author.id]))+'**')
            return None 
        #if specific category requested, show only the expenses in given category
        elif category:
            await ctx.send(category_report(ctx, category)[0], ephemeral=True)           
        #if no arguments passed, show all expenses
        else:
            await ctx.send(all_expenses_report(ctx), ephemeral=True)

    @commands.command(name="love",
                      brief="- money buddy loves you too")
    async def love(self, ctx: commands.Context, *args: str):
        await ctx.send("I love you too :)")

async def setup(client):
    await client.add_cog(View(client))
