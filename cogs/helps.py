from turtle import delay
import discord
from discord.ext import commands, tasks
from cogs import sixmans, Music, birthday
import random
from random import choice
import time
import functools
import itertools
import math
import datetime as dt
import json

class helpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.darker_grey(), timestamp=ctx.message.created_at,
                            title="6Mans:")
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="queue", value="Queues you for 6Mans")
        embed.add_field(name="leavequeue", value=f'Leaves the queue for 6Mans', inline=True)
        embed.add_field(name="seequeue", value=f'Sees the queue for 6Mans', inline=True)
        embed.add_field(name="queueping", value="Pings the queue for 6Mans", inline=True)
        embed.add_field(name="end_game", value="Ends the game and deletes channels for 6Mans", inline=True)
        embed.add_field(name="clear_queue", value="(ADMIN) Clears the queue for 6Mans", inline=False)
        embed.add_field(name="startqueue", value="(ADMIN) Starts the queue for 6Mans", inline=False)
        await ctx.send(embed=embed)
        embed1 = discord.Embed(
            colour=discord.Colour.darker_grey(), timestamp=ctx.message.created_at,
                            title="Music:")
        embed1.set_footer(text=f"Requested by {ctx.author}")

        embed1.add_field(name="join", value="Joins VC", inline=True)
        embed1.add_field(name="leave", value=f'Leaves VC', inline=True)
        embed1.add_field(name="volume {0-100}", value=f'Adjusts Volume', inline=True)
        embed1.add_field(name="Pause", value="Pauses song",inline=True)
        embed1.add_field(name="Resume", value="Resumes song", inline=True)
        embed1.add_field(name="Stop", value="Stops song", inline=True)
        embed1.add_field(name="Clear", value="Clears queue", inline=True)     
        embed1.add_field(name="Skip", value="Vote skip song", inline=True)
        embed1.add_field(name="List", value="Shows queue", inline=True)
        embed1.add_field(name="Shuffle", value="Shuffles queue", inline=True)
        embed1.add_field(name="Remove {Queue #}", value="Removes a song in queue", inline=True)
        embed1.add_field(name="Loop", value="Loops queue", inline=True)
        embed1.add_field(name="Play", value="Plays song", inline=True)
        await ctx.send(embed=embed1)
        embed2 = discord.Embed(
            colour=discord.Colour.darker_grey(), timestamp=ctx.message.created_at,
                            title="Birthday:")
        embed2.set_footer(text=f"Requested by {ctx.author}")
        embed2.add_field(name="bdayhelp", value="How to set birthday", inline=True)
        embed2.add_field(name="setbday {'Name' Day Month Year}", value=f'Sets birthday. formated as 00 00 0000', inline=True)
        await ctx.send(embed=embed2)