import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or(''), intents = intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

async def main():
	try:
		await bot.load_extension("cogs.addExpense")
		await bot.load_extension("cogs.report")
		await bot.load_extension("cogs.categories")
		print(f'Extension loaded!')
	except Exception as e:
		print(f'Failed to load extension cogs.')
		print(str(e))
	await bot.start('MTE1NDk3MDUxNzMwMDg1NDgzNg.Gg5KIR.IroJdSLSFJzv1MHmCxu8CaCfKmw3GU9vpTpSIY')

asyncio.run(main())
