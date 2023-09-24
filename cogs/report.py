from discord.ext import commands
import locale

from .vars import*

# expense report for a category
def category_report(ctx:commands.Context, category: str):
    if not category in expenses[ctx.author.id]:
        return f'"{category}" is not a category', 0
    locale.setlocale(locale.LC_ALL, '')
    report: str = f"**{category}**"
    total: float = 0
    for idx, expense in enumerate(expenses[ctx.author.id][category]):
        report += f"\n\t{idx + 1}) {expense[0]}: {expense[2]} - {locale.currency(expense[1], grouping=True)}"
        total += expense[1]
    report += f"\n\t*TOTAL: {locale.currency(total, grouping=True)}*"
    return report, total

# generates an expense report for all categories
def all_expenses_report(ctx:commands.Context) -> str:
    report: str = ""
    total: float = 0

    for category in expenses[ctx.author.id]:
        cat_rep = category_report(ctx, category)
        report += f"\n{cat_rep[0]}"
        total += cat_rep[1]

    report += f"\n***TOTAL: {locale.currency(total, grouping=True)}***"

    return report

# cog
class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def view(self, ctx: commands.Context, category: str | None):
        if category:
            await ctx.send(category_report(ctx, category)[0], ephemeral=True)           
        else:
            await ctx.send(all_expenses_report(ctx), ephemeral=True)
            
        


# add this cog to the client
async def setup(client):
    await client.add_cog(Report(client))
