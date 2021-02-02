import discord
from discord.ext import commands
from pymongo import MongoClient
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

bot_channel = 806029217384890390
cluster = MongoClient(str(os.getenv("db")))

levelling = cluster["codexBot"]["rankData"]


class levelSystem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Competition cog is ready to roll!!!")
