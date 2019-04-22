import string
import re
import datetime

from discord.ext import commands
import discord

from .util import twow_helper, checks, timed_funcs
from .util.categories import category
from .timer import delta_to_string


class Custom:
    @category('etc')
    @commands.command()
    async def test(self, ctx):
        '''Testing
        '''
        await ctx.bot.send_message(ctx.channel,
            'Just a test,bro.')

def setup(bot):
    bot.add_cog(Custom())
