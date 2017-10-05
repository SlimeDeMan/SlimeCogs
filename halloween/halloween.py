import datetime
from datetime import date
import discord
from discord.ext import commands


class HalloweenClock:
    """Simple display of days left until next halloween"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def halloween(self):
        """Display days left 'til halloween"""

        now = datetime.datetime.now()
        today = date(now.year, now.month, now.day)

        year = now.year
        if (now.month == 10 and now.day > 31):
            year = now.year + 1

        halloween = date(year, 10, 31)

        delta = halloween - today

        await self.bot.say("```" + str(delta.days) + " days left until Halloween!```")


def setup(bot):
    bot.add_cog(HalloweenClock(bot))
