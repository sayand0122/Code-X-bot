# importing all necessary libraries
import discord
from discord.ext import commands, tasks
import dotenv
import os
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()

# setting up a prefix for the bot
client = commands.Bot(command_prefix='.')
client.remove_command('help')

status = cycle(['Bored in the House','Listening to Bad Guy by Billie Eilish','Type commands to see how I function😁','Working on my own code','Stay Safe','College life is Chill'])





# its a function decorator that denotes the function is going to represent an event
@client.event
# its an asynchronous function
# the on_ready() function is like when this bot is in ready state like when it has got all the information from discord
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(client))






# changes the game activity of bot every 30 mins
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))





# errors handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('```Inavlid Command used.```')



# clear commands and its error handling
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass the amount to clear the number of data.")





# ping it and it returns your latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')




# links to various sites
@client.command(aliases=['media'])
async def links(ctx):
    myembed = discord.Embed(title='Links to our Social sites' , description='' , color=discord.Colour.red())
    myembed.add_field(name='Follow us at Instagram' , value='*[Instagram](https://www.instagram.com/codex_gitam "Link to our insta page")*' , inline=False)
    myembed.add_field(name='View our Github Page' , value='*[GitHub](https://github.com/c-code-x "Link to ou github organization")*' , inline=False)
    myembed.add_field(name='Our Website' , value='*[Website](https://google.com "Link to our Code-X website")*' , inline=False)
    await ctx.send(embed=myembed)




# help command
@client.command(aliases=['assist'])
async def help(ctx):
    await ctx.send("```Note - Type the prefix '.' before every command```\n```List of commands\n• .help/.assist\n• .ping \n• .links \n• .whois 'exact core-member name' \n• .clear 'specify amount here \n• .courses \n• .courses 'exact domain name''```")



# maintaining cogs
@client.command()
async def load(ctx, extension):
    client.load_exntension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    client.unload_exntension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')




# after we gave all the info to the bot we need to run this client (in brakets is the unique bot token)
client.run(str(os.getenv("DISCORD_SECRET")))
