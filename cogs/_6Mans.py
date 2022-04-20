from turtle import delay
import discord
from discord.ext import commands, tasks
import random
from random import choice
import time
import functools
import itertools
import math

class sixmans(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.rlqueue = []
        self.max_queue = 6
        self.qtoggle = True
        self.active_games = {}

    @commands.command(aliases=["q"], pass_context=True)
    async def queue(self, ctx):
        ''' Add yourself to the queue!'''
        author = ctx.message.author
        server = ctx.message.guild.id
        user = discord.Member
        if self.qtoggle == False:
            return
        if author in self.rlqueue:
            await ctx.send("You're already in the queue!")
            return
        if author not in self.rlqueue:
            await ctx.send('you have been added to the queue.')

            if len(self.rlqueue) > 6:
               len(self.rlqueue) == len(self.rlqueue) - 1
               return
            else:
                self.rlqueue.append(author)
                mention_members = " ".join([member.mention for member in self.rlqueue])
                embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
                embed.add_field(name='Rocket League Queue: ', value=mention_members .format(mention_members), inline=False)
                await ctx.send(embed=embed)

        if len(f"{self.rlqueue}") == self.max_queue:
            embed = discord.Embed(
                colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value=mention_members, inline=False)
            await ctx.send(f"{embed}")
            self.room_name = self._generate_name_pass()
            self.room_pass = self._generate_name_pass()
            await ctx.send(f"The queue has filled, Please hop in a voice channel and play Rocket League! Please look at new channel for info")
            await self.create_channels(ctx)
            self.rlqueue = []

    @commands.command(aliases=['dq', 'lq'], pass_context=True)
    async def leavequeue(self, ctx):
        author = ctx.message.author
        self.rlqueue.remove(author)
        if self.rlqueue == []:
            embed = discord.Embed(
            colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value="0 Players are in the Queue", inline=False)
            await ctx.send(embed=embed)
        elif author in self.rlqueue:
            mention_members = " ".join([member.mention for member in self.rlqueue])
            await ctx.send(f'you have been removed from the queue.\n')
            embed = discord.Embed(
            colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value=mention_members, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send('you were not in the queue.')

    @commands.command(aliases=['CQ'], pass_context=True)
    async def seequeue(self, ctx):
        if self.rlqueue == []:
            embed = discord.Embed(
            colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value="0 Players are in the Queue", inline=False)
            await ctx.send(embed=embed)
        elif self.rlqueue is not []:
            mention_members = " ".join([member.mention for member in self.rlqueue])
            embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value=mention_members, inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=['clearq'])
    @commands.has_permissions(manage_messages=True)
    async def clear_queue(self, ctx):
        ''' Clears the queue'''
        self.rlqueue = []
        await ctx.send('Queue has been cleared')

    @commands.command(aliases=['startq'])
    @commands.has_guild_permissions(manage_guild=True)
    async def startqueue(self, ctx):
        mention_members = " ".join([member.mention for member in self.rlqueue])
        if self.rlqueue == []:
            await ctx.send("Sorry, no one is in the queue")
        elif self.rlqueue is not []:
            embed = discord.Embed(
                colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value=mention_members, inline=False)
            self.room_name = self._generate_name_pass()
            self.room_pass = self._generate_name_pass()
            await ctx.send(f"||{mention_members}|| \nThe queue has filled, Please hop in a voice channel and play Rocket League! Please look at new channel for info")
            await ctx.send(embed=embed)
            await self.create_channels(ctx)
            self.rlqueue = []

    @commands.command()
    async def queueping(self, ctx):
        await ctx.send(f"{self.rlqueue}, You have been summonned.")

    @commands.command()
    async def end_game(self, ctx):
        await self.delete_channels(ctx)

    async def create_channels(self, ctx):
        mention_members = " ".join([member.mention for member in self.rlqueue])
        category = discord.utils.get(ctx.guild.categories, name="Rocket League")

        tc = await ctx.guild.create_text_channel(f"6mans", category=category)
        bvc = await ctx.guild.create_voice_channel(f"Blue Team",category=category)
        ovc = await ctx.guild.create_voice_channel(f"Orange Team",category=category)
        text_channel = discord.utils.get(ctx.guild.channels, name="6mans")
        channel = discord.utils.get(ctx.guild.channels, name="6mans")
        blue_vc = discord.utils.get(ctx.guild.channels, name="Blue Team")
        orange_vc = discord.utils.get(ctx.guild.channels, name="Orange Team")
        channel = ctx.guild.get_channel(tc.id)
        self.active_games[text_channel] = [blue_vc, orange_vc]
        embed = discord.Embed (
            colour = discord.Colour.red())
         # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='Rocket League Queue: ', value=f'{mention_members}', inline=False)
        embed.add_field(name='Lobby info\nUsername: ', value=f'{self.room_name}', inline=True)
        embed.add_field(name='Lobby info\Password: ', value=f'{self.room_pass}', inline=True)
        embed = embed
        await channel.send(f"{mention_members}", embed=embed)
        

    async def delete_channels(self, ctx):
        for text_channel, voice_channel_list in self.active_games.items():
            # text_channel is the key, and you can use it directly for whatever purpose you have for it
            blue_vc = voice_channel_list[0]
            orange_vc = voice_channel_list[1]
            await ctx.send("Thanks! The VCs and text channel will be deleted after 5 seconds")
            del self.active_games[text_channel]
            time.sleep(5)
            delay(5)
            await blue_vc.delete()
            await orange_vc.delete()
            await text_channel.delete()
            return

    @commands.command(pass_context=True)
    async def queuehelp(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.darker_grey())
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='q', value='Joins the Rocket league Queue', inline=False)
        embed.add_field(name='dq', value='Removes you from the Rocket League Queue', inline=False)
        embed.add_field(name='startqueue', value="See when a user has joined Rocket Wars discord, as well as joined discord. You'll be able to see roles and their ID.", inline=False)
        embed.add_field(name='queueping', value='Pings the queue for starting low number games', inline=False)
        embed.add_field(name='End_Game', value='Ends the game and deletes Channels', inline=False)
        embed.add_field(name='clearqueue', value='Clears the queue *(Need to be mod or higher)*', inline=False)
        embed.add_field(name='Check_Queue_Size (RL_QS, RL_CQS)', value='See how many people are in queue and max queue size', inline=False)
        # embed.add_field(name=' ', value=' ', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def view_queues(self, ctx):
        await ctx.send(f'{self.rlqueue.name}')

    def _generate_name_pass(self):
        return room_pass[random.randrange(len(room_pass))]

    def teams(self, user : discord.Member):
        return [random.randrage(len(self.rlqueue))]

room_pass = [
    'octane', 'takumi', 'dominus', 'hotshot', 'batmobile', 'mantis',
    'paladin', 'twinmill', 'centio', 'breakout', 'animus', 'venom',
    'xdevil', 'endo', 'masamune', 'merc', 'backfire', 'gizmo',
    'roadhog', 'armadillo', 'hogsticker', 'luigi', 'mario', 'samus',
    'sweettooth', 'cyclone', 'imperator', 'jager', 'mantis', 'nimbus',
    'samurai', 'twinzer', 'werewolf', 'maverick', 'artemis', 'charger',
    'skyline', 'aftershock', 'boneshaker', 'delorean', 'esper',
    'fast4wd', 'gazella', 'grog', 'jeep', 'marauder', 'mclaren',
    'mr11', 'proteus', 'ripper', 'scarab', 'tumbler', 'triton',
    'vulcan', 'zippy',

    'aquadome', 'beckwith', 'champions', 'dfh', 'mannfield',
    'neotokyo', 'saltyshores', 'starbase', 'urban', 'utopia',
    'wasteland', 'farmstead', 'arctagon', 'badlands', 'core707',
    'dunkhouse', 'throwback', 'underpass', 'badlands',

    '20xx', 'biomass', 'bubbly', 'chameleon', 'dissolver', 'heatwave',
    'hexed', 'labyrinth', 'parallax', 'slipstream', 'spectre',
    'stormwatch', 'tora', 'trigon', 'wetpaint',

    'ara51', 'ballacarra', 'chrono', 'clockwork', 'cruxe',
    'discotheque', 'draco', 'dynamo', 'equalizer', 'gernot', 'hikari',
    'hypnotik', 'illuminata', 'infinium', 'kalos', 'lobo', 'looper',
    'photon', 'pulsus', 'raijin', 'reactor', 'roulette', 'turbine',
    'voltaic', 'wonderment', 'zomba',

    'unranked', 'prospect', 'challenger', 'risingstar', 'allstar',
    'superstar', 'champion', 'grandchamp', 'bronze', 'silver', 'gold',
    'platinum', 'diamond',

    'dropshot', 'hoops', 'soccar', 'rumble', 'snowday', 'solo',
    'doubles', 'standard', 'chaos',

    'armstrong', 'bandit', 'beast', 'boomer', 'buzz', 'cblock',
    'casper', 'caveman', 'centice', 'chipper', 'cougar', 'dude',
    'foamer', 'fury', 'gerwin', 'goose', 'heater', 'hollywood',
    'hound', 'iceman', 'imp', 'jester', 'junker', 'khan', 'marley',
    'maverick', 'merlin', 'middy', 'mountain', 'myrtle', 'outlaw',
    'poncho', 'rainmaker', 'raja', 'rex', 'roundhouse', 'sabretooth',
    'saltie', 'samara', 'scout', 'shepard', 'slider', 'squall',
    'sticks', 'stinger', 'storm', 'sultan', 'sundown', 'swabbie',
    'tex', 'tusk', 'viper', 'wolfman', 'yuri']