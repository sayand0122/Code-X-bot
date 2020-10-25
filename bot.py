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



@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguements.")
@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass the amount to clear the number of data.")



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



# we use parenthesis her coz there are couple of commands we want to change for example we want specific commands to be hidden from user
@client.command(aliases=['media'])
async def links(ctx):
    await ctx.send("```Follow us at Instagram : -``` https://www.instagram.com/codex_gitam")
    await ctx.send("```Catchup with us on our website : -``` ")
    await ctx.send("```View our Github Page : -``` https://github.com/c-code-x")




@client.command(aliases=['assist'])
async def help(ctx):
    await ctx.send("```Note - Type the prefix '.' before every command```\n```List of commands\n•assist/help\n•ping\n•links\n•team 'core member name'\n•clear 'specify amount here'```")




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
