import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random
from random import choice
import time
import functools
import itertools
import math
import ffmpeg
from cogs import sixmans, Music, birthday, helpy
from async_timeout import timeout
from discord.voice_client import VoiceClient
import os

intents = discord.Intents.all() # Imports all the Intents
directory = os.path.dirname(os.path.realpath(__file__))
client = commands.Bot(command_prefix = ".", case_insensitive=True, intents=intents)

async def main():
    print(f'started at {time.strftime(("%a, %#d %B %Y, %I:%M %p ET"))}')
asyncio.run(main())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help | Testing in progress ...'))
    print('The Bot is running!')
    client.add_cog(sixmans(client))
    client.add_cog(Music(client))
    client.add_cog(birthday(client))
    client.add_cog(helpy(client))

@client.event 
async def on_command_error(ctx, ERROR):
    await ctx.send(ERROR)
    print(ERROR)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong\nbot took around {round(client.latency * 1000)}ms to respond")

@client.command()
async def dm(ctx, user: discord.User, *, msg):
    embed = discord.Embed(
        color=0x336EFF
        )
    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
    embed.add_field(name=f"Direct message from: {ctx.guild}", value=f"{msg}", inline=False)
    embed.set_footer(text=f'from {ctx.author}')
    await user.send(embed=embed)
    await ctx.send("Done!")

@client.command()
async def dice(ctx):
    dice1=random.randrange(0,6)
    dice2=random.randrange(0,6)
    dice3=random.randrange(0,6)
    dice4=random.randrange(0,6)
    count1=dice1+dice2
    count2=dice3+dice4
    await ctx.send(f"Your dice rolled are {dice1}, and {dice2}.")
    await ctx.send(f"{ctx.author.display_name}, your opponent rolls a {dice3} and {dice4}.")
    if count1>count2:
        await ctx.send(f"**{ctx.author.display_name}**, You've won!")
        return
    elif count2>count1:
        await ctx.send(f"**{ctx.author.display_name}**, Sorry, you lost. Please try again!")
        return
    elif count1==count2:
        await ctx.send(f"**{ctx.author.display_name}**, It's a draw, Please try again!")
    else:
        return
client.remove_command('help')
client.run("")