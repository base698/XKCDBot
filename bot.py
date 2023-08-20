import os 
import discord
from discord.ext import commands
import search

intents = discord.Intents.default()  # Create a new Intents object with default flags enabled
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def xkcd(ctx, arg):
    print("command here", ctx, arg)
    await ctx.send(arg)

# Event for on_message
@bot.event
async def on_message(message):
    print(f'{message.author} {bot.user}')
    if message.author == bot.user:
        return

    if not message.content.startswith('!') and message.content:
        results = search.search_xkcd(message.content, n=5, pprint=False)
        results = results[results['similarity']>0.79]
        if len(results) > 0:
           top_hit = results.index.values.astype(str)[0] # get the index id (the comic number)
           await message.channel.send(f'https://xkcd.com/{top_hit}/')

# Run the bot
bot.run(os.environ.get('BOT_TOKEN'))
