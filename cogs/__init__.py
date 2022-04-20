import discord
from ._6Mans import sixmans
from .musique import Music
from .bday import birthday
from .helps import helpy
def setup(bot):
    bot.add_cog(sixmans(bot))
    bot.add_cog(Music(bot))
    bot.add_cog(birthday(bot))
    bot.add_cog(helpy(bot))