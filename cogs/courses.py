import discord
from discord.ext import commands

class courses(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Courses cog is ready")

    @commands.command()
    async def courses(self, ctx, message):
        if message == "beginners":
            e=discord.Embed(title='Courses',description='',color=0x140ec7)
            await ctx.send(embed=e)




    @courses.error
    async def courses_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Please pass an argument from below so that you get exact results\n -beginners \n -DSA \n -CP question \n -frontend \n -backend \n -version control \n -ML \n -App Dev \n```')


def setup(client):
    client.add_cog(courses(client))