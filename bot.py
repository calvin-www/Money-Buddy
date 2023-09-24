import discord
from discord.ext import commands
import asyncio
from collections import defaultdict

#allows the bot to do anything it needs
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or(''), intents = intents)

@bot.event
async def on_ready():
	#outputs who the bot is in the terminal
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

async def main():
	try:
		#import all cogs
		await bot.load_extension("cogs.add")
		await bot.load_extension("cogs.view")
		await bot.load_extension("cogs.edit")
		await bot.load_extension("cogs.export")
		await bot.load_extension("cogs.remove")
		print(f'All extensions loaded!')
	# edge case if something goes wrong during import of cogs
	except Exception as e:
		print(f'Failed to load extension cogs.')
		print(str(e))
	#token of specific bot
	await bot.start('MTE1NDk4MTk2MzY0NDU0NzEzMg.GBTMb8.OZGGh8IBy-lkwNgDN3XHHt2AlIxZhaYUsFwfdU')

asyncio.run(main())
