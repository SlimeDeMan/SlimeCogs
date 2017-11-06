import datetime
from datetime import date
import discord
from discord.ext import commands


class NewYear:
    """Simple display of days left until new year"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def newyear(self):
        """Display days left 'til new year"""

        now = datetime.datetime.now()
        today = date(now.year, now.month, now.day)

        year = now.year
        if (now.month == 12 and now.day > 31):
            year = now.year + 1

        year = date(year, 12, 31)

        delta = year - today

        await self.bot.say("```" + str(delta.days) + " days left until New Year!```")


def setup(bot):
    bot.add_cog(NewYear(bot))
