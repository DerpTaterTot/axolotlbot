# admin.py
# discord imports
import discord
from discord.ext import commands
from datetime import datetime

DARKPINK = 0xe75480

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='mute', help="mutes them")
    @commands.has_any_role(769171897564004362, 757966937769902262, 765183925886124032)
    async def mute(self, ctx, user: discord.Member):
        muted = ctx.guild.get_role(764878992737828876)
        logs = self.bot.get_channel(800417369548914708)
        alreadyMuted = None

        mutedEmbed = discord.Embed(color=DARKPINK, timestamp=datetime.utcnow()) 
        if muted in user.roles:
            mutedEmbed.title = "the user is already muted"
            alreadyMuted = True
        else:
            await user.add_roles(muted)
            mutedEmbed.title = f"{user.name} was muted"

        await ctx.send(embed = mutedEmbed)
        if not alreadyMuted:
            await logs.send(f"{ctx.author.name} muted {user.name}")

    @commands.command(name='unmute', help="unmutes them")
    @commands.has_any_role(769171897564004362, 757966937769902262, 765183925886124032)
    async def unmute(self, ctx, user: discord.Member):
        muted = ctx.guild.get_role(764878992737828876)

        unmuteEmbed = discord.Embed(color = DARKPINK, timestamp=datetime.utcnow())
        if muted not in user.roles:
            unmuteEmbed.title = "the user is already unmuted"
        else:
            await user.remove_roles(muted)
            unmuteEmbed.title = f"{user.name} was unmuted"

        await ctx.send(embed = unmuteEmbed)

    @commands.command(name='mediamute', help="mutes them from media")
    @commands.has_any_role(769171897564004362, 757966937769902262, 765183925886124032)
    async def mediamute(self, ctx, user: discord.Member):
        mediamute = ctx.guild.get_role(804007659229544449)
        
        mediamuteEmbed = discord.Embed(color = DARKPINK, timestamp = datetime.utcnow())
        if mediamute in user.roles:
            mediamuteEmbed.title = "that user is already muted from media"
        else:
            mediamuteEmbed.title = f"{user.name} was muted from sending media"
            await user.add_roles(mediamute)
        
        await ctx.send(embed=mediamuteEmbed)

    @commands.command(name='mediaunmute', help="unmutes them from media")
    @commands.has_any_role(769171897564004362, 757966937769902262, 765183925886124032)
    async def mediaunmute(self, ctx, user: discord.Member):
        unmediamute = ctx.guild.get_role(804007659229544449)

        unmediamuteEmbed = discord.Embed(color = DARKPINK, timestamp = datetime.utcnow())
        if unmediamute not in user.roles:
            unmediamuteEmbed.title = "that user is already unmuted from media"
        else:
            unmediamuteEmbed.title = f"{user.name} was unmuted from sending media"
            await user.remove_roles(unmediamute)
        
        await ctx.send(embed=unmediamuteEmbed)
    
