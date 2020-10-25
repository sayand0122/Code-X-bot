# importing all necessary libraries
import discord
from discord.ext import commands
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

# setting up a prefix for the bot
client = commands.Bot(command_prefix='.')

# its a function decorator that denotes the function is going to represent an event


@client.event
# its an asynchronous function
# the on_ready() function is like when this bot is in ready state like when it has got all the information from discord
async def on_ready():
    print('Bot is on the way!!!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# we use parenthesis her coz there are couple of commands we want to change for example we want specific commands to be hidden from user


@client.command(aliases=['media'])
async def links(ctx):
    await ctx.send("```Follow us at Instagram : -``` https://www.instagram.com/codex_gitam")
    await ctx.send("```Catchup with us on our website : -``` ")
    await ctx.send("```View our Github Page : -``` https://github.com/c-code-x")


@client.command()
async def team(ctx):
    await ctx.send('App Development\n``` Jaideep \n Bhargav``` \n Competitive Coding ```\n Sayan``` \n AI/ML ```\n Srinija \n Neeraj``` \n Frontend ```\n Navya \n Madhulika``` \n Content Writting ```\n Nitisha``` \n Public Relation ```\n Manoj```')


@client.command(aliases=['sayan'])
async def cp(ctx):
    await ctx.send('```bash\n"Heya guys nice to meet you all. I am Sayan and we can have lots of fun together"```')
    await ctx.send('``` You can follow me up on github : -``` https://github.com/sayand0122')
    await ctx.send('``` Wanna connect with me on LinkedIn : -``` https://www.linkedin.com/in/sayan-dutta-117a8a1a8/')


@client.command(aliases=['darkquill'])
async def cw(ctx):
    await ctx.send('```css\n[Hi guys nice to meet you all. I am Nishitha]```')
    await ctx.send('``` Lets connect on LinkedIn : -``` https://www.linkedin.com/in/nishitha-motakatla-187465193/')


@client.command(aliases=['manoj'])
async def pr(ctx):
    await ctx.send('```ini\n[Hi guys! Great to see you all. I am Manoj]```')
    await ctx.send('``` Connect with me on LinkedIn : -```  https://www.linkedin.com/in/k-manoj-manu-4224941ba')


@client.command()
async def srinijads(ctx):
    await ctx.send(" ```fix\nI'm Srinija and I like to code.``` ")
    await ctx.send('``` You can follow me up on github : -``` https://github.com/srinijadharani')
    await ctx.send('``` Wanna connect with me on LinkedIn : -``` https://www.linkedin.com/in/srinijadharani/')


@client.command()
async def loganwick(ctx):
    await ctx.send("```diff\n+ Hey guys Jai this side U can call me logan😁```")
    await ctx.send('``` Checkout my github : -``` https://github.com/Jaideep-C')
    await ctx.send('``` Connect with me on LinkedIn : -``` https://www.linkedin.com/in/jaideep-c-807413138/')


@client.command()
async def navya(ctx):
    await ctx.send("```diff\n- Yeoboseyo I'm Navya let's  work together and learn together```")
    await ctx.send('``` Github : -``` https://github.com/navya-005')
    await ctx.send("``` Let's connect on LinkedIn : -``` https://www.linkedin.com/in/navyasree-mallela-b0a4931ba/")


@client.command()
async def bharxhav(ctx):
    await ctx.send("```diff\n+ Hello there! Bhargav here.```")
    await ctx.send('``` My github : -``` https://github.com/bharxhav')
    await ctx.send('``` LinkedIn here : -``` https://www.linkedin.com/in/bhargavkantheti/')


@client.command()
async def neeraj(ctx):
    await ctx.send("```fix\nHey guys Neeraj this side.```")
    await ctx.send('``` Github : -``` https://github.com/NEERAJAP2001')
    await ctx.send('``` LinkedIn : -``` https://www.linkedin.com/in/neeraj-adityananth/')


@client.command()
async def madhulika(ctx):
    await ctx.send("```diff\n- I'm Madhulika```")
    await ctx.send('``` You can follow me up on github : -``` https://github.com/madhulika01')
    await ctx.send('``` Wanna connect with me on LinkedIn : -``` https://www.linkedin.com/in/madhulika-akumalla-a984ab1ba/')


# after we gave all the info to the bot we need to run this client (in brakets is the unique bot token)
client.run(str(os.getenv("DISCORD_SECRET")))
