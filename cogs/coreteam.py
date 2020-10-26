import discord
from discord.ext import commands
from discord.guild import Guild
from discord import role

class coreteam(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")
    

    #Commands
    @commands.command()
    async def whois(self, ctx, member : discord.Member):
        if member.nick == "Sayan":
            e = discord.Embed(title = member.nick , description = 'Heya guys nice to meet you all. I am Sayan and we can have lots of fun together' , color = 0x140ec7)
            e.add_field(name='My projects expo',value=' https://github.com/sayand0122',inline=False)
            e.add_field(name='Socialization spot',value='https://www.linkedin.com/in/sayan-dutta-117a8a1a8/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)
        
        elif member.name=="Loganwick":
            e = discord.Embed(title = member.name , description = 'Hey guys Jai this side U can call me logan😁' , color = 0x1cc70c)
            e.add_field(name='You can follow me up on github',value='https://github.com/Jaideep-C',inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',value='https://www.linkedin.com/in/jaideep-c-807413138/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name=="srinijads":
            e = discord.Embed(title = member.name , description = "I'm Srinija and I like to code." , color = 0xf0e118)
            e.add_field(name='Way to my github',value='https://github.com/srinijadharani',inline=False)
            e.add_field(name='LinkedIn',value='https://www.linkedin.com/in/srinijadharani/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name=="NeerajAP":
            e = discord.Embed(title = member.name , description = "Hey guys Neeraj this side." , color = 0xf0e118)
            e.add_field(name='My projects',value='https://github.com/NEERAJAP2001',inline=False)
            e.add_field(name='LinkedIn',value='https://www.linkedin.com/in/neeraj-adityananth/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)
            
        elif member.name=="bharxhav":
            e = discord.Embed(title = member.name , description = "Hi Bhargav here." , color = 0x1cc70c)
            e.add_field(name='You can follow me up on github',value='https://github.com/bharxhav',inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',value='https://www.linkedin.com/in/bhargavkantheti/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name=="Navya":
            e = discord.Embed(title = member.name , description = " Yeoboseyo I'm Navya let's work together and learn together" , color = 0xdb142b)
            e.add_field(name='You can follow me up on github',value='https://github.com/navya-005',inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',value=' https://www.linkedin.com/in/navyasree-mallela-b0a4931ba/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name=="Madhulika":
            e = discord.Embed(title = member.name , description = "I'm Madhulika" , color = 0xdb142b)
            e.add_field(name='You can follow me up on github',value='https://github.com/madhulika01',inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',value='https://www.linkedin.com/in/madhulika-akumalla-a984ab1ba/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)
           
        elif member.name=="Dark Quill":
            e = discord.Embed(title = member.name , description = "Hi guys nice to meet you all. I am Nishitha" , color = 0xdb6714)
            e.add_field(name='Link to my LinkedIn',value='https://www.linkedin.com/in/nishitha-motakatla-187465193/',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name=="Manoj":
            e = discord.Embed(title = member.name , description = "Hi guys! Great to see you all. I am Manoj" , color = 0x1156a6)
            e.add_field(name='My LinkedIn',value='https://www.linkedin.com/in/k-manoj-manu-4224941ba',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)
        
        elif member.name=="Nanda":
            e = discord.Embed(title = member.name , description = "Hi buddies Nanda here." , color = 0xdb142b)
            e.add_field(name='My Github',value='',inline=False)
            e.add_field(name='My LinkedIn',value='',inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)
    

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass the exact coreteam member name.")


def setup(client):
    client.add_cog(coreteam(client))