import discord
from discord.ext import commands

class coreteam(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")
    
    #Commands
    @commands.command()
    async def team(self, ctx, member):
        if member=="sayan":
            await ctx.send('```bash\n"Heya guys nice to meet you all. I am Sayan and we can have lots of fun together"```')
            await ctx.send('``` You can follow me up on github : -``` https://github.com/sayand0122')
            await ctx.send('``` Wanna connect with me on LinkedIn : -``` https://www.linkedin.com/in/sayan-dutta-117a8a1a8/')

        elif member=="loganwick":
            await ctx.send("```diff\n+ Hey guys Jai this side U can call me logan😁```")
            await ctx.send('``` Checkout my github : -``` https://github.com/Jaideep-C')
            await ctx.send('``` Connect with me on LinkedIn : -``` https://www.linkedin.com/in/jaideep-c-807413138/')

        elif member=="srinijads":
            await ctx.send(" ```fix\nI'm Srinija and I like to code.``` ")
            await ctx.send('``` You can follow me up on github : -``` https://github.com/srinijadharani')
            await ctx.send('``` Wanna connect with me on LinkedIn : -``` https://www.linkedin.com/in/srinijadharani/')

        elif member=="neeraj":
            await ctx.send("```fix\nHey guys Neeraj this side.```")
            await ctx.send('``` Github : -``` https://github.com/NEERAJAP2001')
            await ctx.send('``` LinkedIn : -``` https://www.linkedin.com/in/neeraj-adityananth/')

        elif member=="barxhav":
            await ctx.send("```diff\n+ Hi Bharghav here.```")
            await ctx.send('``` My github : -``` https://github.com/bharxhav')
            await ctx.send('``` LinkedIn here : -``` https://www.linkedin.com/in/bhargavkantheti/')

        elif member=="navya":
            await ctx.send("```diff\n- Yeoboseyo I'm Navya let's  work together and learn together```")
            await ctx.send('``` Github : -``` https://github.com/navya-005')
            await ctx.send("``` Let's connect on LinkedIn : -``` https://www.linkedin.com/in/navyasree-mallela-b0a4931ba/")

        elif member=="madhulika":
            await ctx.send("```diff\n- I'm Madhulika```")
            await ctx.send('``` You can follow me up on github : -``` https://github.com/madhulika01')
            await ctx.send('``` Wanna connect with me on LinkedIn : -``` https://www.linkedin.com/in/madhulika-akumalla-a984ab1ba/')

        elif member=="darkquill":
            await ctx.send('```css\n[Hi guys nice to meet you all. I am Nishitha]```')
            await ctx.send('``` Lets connect on LinkedIn : -``` https://www.linkedin.com/in/nishitha-motakatla-187465193/')

        elif member=="manoj":
            await ctx.send('```ini\n[Hi guys! Great to see you all. I am Manoj]```')
            await ctx.send('``` Connect with me on LinkedIn : -```  https://www.linkedin.com/in/k-manoj-manu-4224941ba')


def setup(client):
    client.add_cog(coreteam(client))