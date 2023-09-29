import discord
from discord.ext import commands
import asyncio
from collections import defaultdict
from cogs.add import addCategory
from find_receipt import *
from cogs.vars import *

#allows the bot to do anything it needs
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = commands.when_mentioned_or(''), intents = intents)

@bot.event
async def on_ready():
	#outputs who the bot is in the terminal
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

@bot.event
async def on_message(message):
	if message.attachments:
		if len(message.content)==0:
			return await message.channel.send("When uplpoading a reciept to scan, you have to send the category and description(optional) in that order.")
		
		url = message.attachments[0].url
		text = read_receipt_url(url)
		total = find_total(text)
		date = find_date(text)
		
		args = message.content.split()
		category = args[0]
		desc = ""
		ctx = message
		if len(args)>=2:
				desc = " ".join(args[1:])
		if category not in expenses[ctx.author.id]:
				await addCategory(ctx, args)
		if [date, total, desc] in expenses[ctx.author.id][category]:
				return await message.channel.send("Sorry, you added that expense previously")
		try:
				total=float(total)
		except Exception as e:
				total=0
		
		if total <= 0.0:
				return await message.channel.send("Try again. The amount has to be just a number.")
		expenses[ctx.author.id][category].append([date, total, desc])
		update_db()
		return await ctx.channel.send(f"New {args[0]} expense added!")
	await bot.process_commands(message)
       
		

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
	await bot.start('MTE1NDk4MTk2MzY0NDU0NzEzMg.GKHxMO.nS2A1i8aixeBfVCT_QAYAwQ3rLawGHRMkK5Ero')

asyncio.run(main())