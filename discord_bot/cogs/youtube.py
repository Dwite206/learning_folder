import discord
from discord.ext import commands
import requests


class _Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # <---- Writes out if youtube.py was correctly loaded ---->
    @commands.Cog.listener()
    async def on_ready(self):
        print("youtube.py was succesfully loaded!")


def setup(bot):
    bot.add_cog(_Youtube(bot))
