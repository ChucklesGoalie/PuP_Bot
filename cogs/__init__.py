import discord
from ._6Mans import sixmans
from .musique import Music
from .bday import birthday
def setup(bot):
    bot.add_cog(sixmans(bot))
    bot.add_cog(Music(bot))
    bot.add_cog(birthday(bot))