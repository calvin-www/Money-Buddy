from discord.ext import commands
import locale

from .vars import expenses

# expense report for a category
def category_report(category: str):
    if not category in expenses:
        return f'"{category}" is not a category', 0

    locale.setlocale(locale.LC_ALL, '')

    report: str = f"**{category}**"
    total: float = 0
    for idx, expense in enumerate(expenses[category]):
        print(idx, expense)
        report += f"\n\t{idx + 1}) {expense[0]}: {expense[2]} - {locale.currency(expense[1], grouping=True)}"
        print(report)
        total += expense[1]
    report += f"\n\t*TOTAL: {locale.currency(total, grouping=True)}*"

    return report, total

# generates an expense report for all categories
def all_expenses_report() -> str:
    report: str = ""
    total: float = 0

    for category in expenses:
        cat_rep = category_report(category)
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
            await ctx.send(category_report(category)[0], ephemeral=True)           
        else:
            await ctx.send(all_expenses_report(), ephemeral=True)
            
        


# add this cog to the client
async def setup(client):
    await client.add_cog(Report(client))
