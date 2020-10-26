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
            e=discord.Embed(title='Getting Started with basics of CODING',description='',color=0x12cc91)
            e.add_field(name='C++',value='*[GeeksforGeeks](https://www.geeksforgeeks.org/c-plus-plus/)*\n*[W3Schools](https://www.w3schools.com/cpp/)*\n*[Video link 1](https://www.youtube.com/watch?v=18c3MTX0PK0&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)*\n*[Video link 2](https://www.youtube.com/watch?v=vLnPwxZdW4Y)*',inline=False)
            e.add_field(name='Java',value='*[Udemy Course](https://www.udemy.com/course/java-tutorial/)*\n*[TutorialsPoint](https://www.tutorialspoint.com/java/index.htm)*\n*[Video link 1](https://www.youtube.com/watch?v=eIrMbAQSU34)*\n*[Video link 2](https://www.youtube.com/watch?v=Qgl81fPcLc8)*',inline=False)
            e.add_field(name='Python',value='*[Udemy Course](https://www.udemy.com/course/complete-python-bootcamp/)*\n*[GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/)*\n*[TutorialsPoint](https://www.tutorialspoint.com/python/index.htm)*\n*[Video Link](https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3)*',inline=False)
            await ctx.send(embed=e)
        
        elif message == "DSA":
            e=discord.Embed(title='Data Structure and Algorithms Storehouse',description='',color=0xe31037)
            e.add_field(name='Algoexpert',value='[DSA](https://www.1377x.to/torrent/4301420/Premium-AlgoExpert-Become-an-Algorithms-Expert/)\n[Algorithms](https://drive.google.com/drive/folders/1ebr3HtTbrdGIs2qxkQIvZ4PEc4uMGuIn?usp=sharing)',inline=False)
            e.add_field(name='SWE',value='[Here](https://drive.google.com/drive/folders/1j-1zeOcY8xcevVS3Fm9kkPbxZ4ofBHze?usp=sharing)')
            e.add_field(name='Algorithms',value='[Here](https://drive.google.com/drive/u/0/folders/1szZmcER2CjAFbcqCLitTn_4nyv0wxUjn?direction=a)',inline=False)
            e.add_field(name='SDE',value='[SDE Problems](https://docs.google.com/document/d/1SM92efk8oDl8nyVw8NHPnbGexTS9W-1gmTEYfEurLWQ/edit)',inline=False)
            await ctx.send(embed=e)

        elif message == "CP":
            e=discord.Embed(title='Competitive coding section',descripton='',color=0x107ae3)
            e.add_field(name='Series',value='[Getting Started](https://www.youtube.com/playlist?list=PL4PCksYQGLJOcaPLgeMFaxaHigPFjBuTG)',inline=False)
            e.add_field(name='Advanced Algo',value='[Recursion1](https://www.geeksforgeeks.org/recursion/)\n[Recursion2](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY)\n[Stacks1](https://www.geeksforgeeks.org/stack-in-cpp-stl/)\n[Stacks2](https://www.youtube.com/playlist?list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd)\n[DP](https://www.geeksforgeeks.org/dynamic-programming/)\n[Dynamic Programming](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)',inline=False)
            e.add_field(name='Java',value='[Tricks](https://www.geeksforgeeks.org/java-tricks-competitive-programming-java-8/)',inline=False)
            e.add_field(name='Hackerrank',value='[Question Set](https://www.hackerrank.com/domains/algorithms)\n[Python Question Set](https://www.hackerrank.com/domains/python)',inline=False)
            await ctx.send(embed=e)

        elif message == "frontend":
            e=discord.Embed(title='FrontEnd - Beginning of Web-Dev',description='[HTML & CSS](https://learn.shayhowe.com/html-css/building-your-first-web-page/)\n[Total Package](https://www.w3schools.com/default.asp)\n[Jumbo Package in Hindi](https://www.youtube.com/watch?v=6mbwJ2xhgzM&list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg)',color=0xde3618)
            e.add_field(name='HTML',value='[Videos](https://www.youtube.com/watch?v=yTHTo28hwTQ&list=PLgGbWId6zgaWZkPFI4Sc9QXDmmOWa1v5F)\n[Study Material](https://www.w3schools.com/default.asp)',inline=False)
            e.add_field(name='CSS',value='[Videos](https://www.youtube.com/watch?v=yTHTo28hwTQ&list=PLgGbWId6zgaWZkPFI4Sc9QXDmmOWa1v5F)\n[Study Material](https://www.w3schools.com/css/default.asp)',inline=False)
            e.add_field(name='JavaScript',value='[Videos](https://www.youtube.com/watch?v=W6NZfCO5SIk)\n[Study Material](https://www.w3schools.com/js/default.asp)',inline=False)
            e.add_field(name='Bootstrap',value='[Videos](https://www.youtube.com/watch?v=QAgrHLtG1Yk&list=PL4cUxeGkcC9jE_cGvLLC60C_PeF_24pvv)\n[Study Material](https://www.w3schools.com/bootstrap4/default.asp)',inline=False)
            await ctx.send(embed=e)
        
        elif message == "ml":
            e=discord.Embed(title='AI the new norm',description='',color=0xe3c414)
            e.add_field(name='Courses',value='[Udemy](https://www.udemy.com/course/machinelearning/)\n[Coursera](https://www.coursera.org/learn/machine-learning)',inline=False)
            e.add_field(name='Video Links',value='[Link1](https://www.youtube.com/watch?v=gmvvaobm7eQ&list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw)\n[Link2](https://www.youtube.com/watch?v=8Oog7TXHvFY&list=PL5-da3qGB5IA_x9xJ7qzUyU1XJwOJsFAn)',inline=False)
            e.add_field(name='Study Material',value='[Most used ML algo](https://www.analyticsvidhya.com/blog/2017/09/common-machine-learning-algorithms/)\n[Tour to ML algos](https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/)',inline=False)
            await ctx.send(embed=e)


    @courses.error
    async def courses_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Please pass an argument from below so that you get exact results\n -beginners \n -DSA \n -CP \n -frontend \n -ml \n\n For ex - .courses ml```')


def setup(client):
    client.add_cog(courses(client))