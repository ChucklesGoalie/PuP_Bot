from turtle import delay
import discord
from discord.ext import commands, tasks
import random
from random import choice
import time
import functools
import itertools
import math
import datetime as dt
import json


class birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bdayhelp(self, ctx):
        await ctx.send("Send your birthday info like this \n'Chuckles Goalie' 13 11 2000")

    @commands.command()
    async def setbday(self, ctx, Name, Day, Month, Year):
        with open("PuP-Bday.json", 'w+') as f:
            data = Name, Day, Month, Year
            await ctx.send(f"Is this right? Answer 'Yes' or 'No' \n {data}")
            await input()
            if input()=="Yes" or "yes":
                await ctx.send('Thank you! This will go into the database.')
                json.dumps(json.load(f), data)
            elif input()=="No" or "no":
                await ctx.send('Cancelling, please re-try the command again to correctly get the data.')
                return
