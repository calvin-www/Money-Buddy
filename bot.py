import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('.'), intents = intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

async def main():
	try:
		await bot.load_extension("cogs.util")
		await bot.load_extension("cogs.addExpense")
		await bot.load_extension("cogs.report")
		print(f'Extension loaded!')
	except Exception as e:
		print(f'Failed to load extension cogs.')
		print(str(e))
	await bot.start('MTE1NDk4MTk2MzY0NDU0NzEzMg.GBTMb8.OZGGh8IBy-lkwNgDN3XHHt2AlIxZhaYUsFwfdU')

asyncio.run(main())

