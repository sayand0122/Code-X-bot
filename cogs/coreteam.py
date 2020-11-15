import discord
from discord.ext import commands
from discord.guild import Guild
from discord import role


class coreteam(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("CoreTeam cog is ready")

    # Commands

    @commands.command()
    async def whois(self, ctx, member: discord.Member):
        if member.nick == "Sayan":
            e = discord.Embed(
                title=member.nick, description='Heya guys nice to meet you all. I am Sayan and we can have lots of fun together', color=0x140ec7)
            e.add_field(name='My projects bundle',
                        value='**[GitHub](https://github.com/sayand0122)**', inline=False)
            e.add_field(name='Socialization spot',
                        value='**[LinkedIn](https://www.linkedin.com/in/sayan-dutta-117a8a1a8/)**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            e.set_footer(icon_url=ctx.author.avatar_url,
                         text=f'Requested by {ctx.author.name}')
            await ctx.send(embed=e)

        elif member.name == "Loganwick":
            e = discord.Embed(
                title=member.name, description='Hey guys Jai this side U can call me logan😁', color=0x1cc70c)
            e.add_field(name='You can follow me up on github',
                        value='**[Here](https://github.com/Jaideep-C "Explore my projects here")**', inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',
                        value='**[Here](https://www.linkedin.com/in/jaideep-c-807413138/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "srinija":
            e = discord.Embed(
                title=member.name, description="I'm Srinija and I like to code.", color=0xf0e118)
            e.add_field(name='Way to my github',
                        value='**[Here](https://github.com/srinijadharani "Explore my projects")**', inline=False)
            e.add_field(
                name='LinkedIn', value='**[Here](https://www.linkedin.com/in/srinijadharani/ "Connect with me")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "NeerajAP":
            e = discord.Embed(
                title=member.name, description="Hey guys Neeraj this side.", color=0xf0e118)
            e.add_field(
                name='My projects', value='**[Here](https://github.com/NEERAJAP2001 "Explore my projects here")**', inline=False)
            e.add_field(
                name='LinkedIn', value='[Here](https://www.linkedin.com/in/neeraj-adityananth/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "bharxhav":
            e = discord.Embed(title=member.name,
                              description="Hi Bhargav here.", color=0x1cc70c)
            e.add_field(name='You can follow me up on github',
                        value='**[Here](https://github.com/bharxhav "Explore my projects here")**', inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',
                        value='**[Here](https://www.linkedin.com/in/bhargavkantheti/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "Navya":
            e = discord.Embed(
                title=member.name, description=" Yeoboseyo I'm Navya let's work together and learn together", color=0xdb142b)
            e.add_field(name='You can follow me up on github',
                        value='**[Here](https://github.com/navya-005 "Explore my projects here")**', inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',
                        value='**[Here](https://www.linkedin.com/in/navyasree-mallela-b0a4931ba/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "Madhulika":
            e = discord.Embed(title=member.name,
                              description="I'm Madhulika", color=0xdb142b)
            e.add_field(name='You can follow me up on github',
                        value='**[Here](https://github.com/madhulika01 "Explore my projects here")**', inline=False)
            e.add_field(name='Wanna connect with me on LinkedIn',
                        value='**[Here](https://www.linkedin.com/in/madhulika-akumalla-a984ab1ba/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "DarkQuill":
            e = discord.Embed(
                title=member.name, description="Hi guys nice to meet you all. I am Nishitha", color=0xdb6714)
            e.add_field(name='Link to my LinkedIn',
                        value='**[Click Here](https://www.linkedin.com/in/nishitha-motakatla-187465193/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.nick == "Manoj":
            e = discord.Embed(
                title=member.name, description="Hi guys! Great to see you all. I am Manoj", color=0x1156a6)
            e.add_field(
                name='My LinkedIn', value='**[Click Here](https://www.linkedin.com/in/k-manoj-manu-4224941ba "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

        elif member.name == "Nanda":
            e = discord.Embed(
                title=member.name, description="A self-taught web developer, gearing toward the field of AI/ML. A passionate coder who loves exploring every aspect of tech.", color=0xdb142b)
            e.add_field(
                name='My Github', value='**[Here](https://github.com/nandaraj2001 "Explore my projects here")**', inline=False)
            e.add_field(
                name='My LinkedIn', value='**[Here](https://www.linkedin.com/in/nanda-rajesh/ "Connect with me here")**', inline=False)
            e.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=e)

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(" ``` Please pass the exact coreteam member name.\n For ex - .whois srinijads```")


def setup(client):
    client.add_cog(coreteam(client))
