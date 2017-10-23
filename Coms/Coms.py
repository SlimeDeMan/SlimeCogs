 import discord
from discord.ext import commands

class Coms:
    """Displays how many cogs and commands there are."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coms(self):
        """Displays how many cogs and commands there are."""

        #Your code will go here
  await self.bot.say("{}/{} active cogs with {} commands".format(
            len(bot.cogs), total_cogs, len(bot.commands)))

def setup(bot):
    bot.add_cog(Coms(bot))