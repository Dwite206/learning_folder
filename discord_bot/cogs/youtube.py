import discord
from discord.ext import commands
import requests
import youtube_dl


class _Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # <---- Writes out if youtube.py was correctly loaded ---->
    @commands.Cog.listener()
    async def on_ready(self):
        print("youtube.py was succesfully loaded!")

    # @commands.command()
    # async def my_hook(self, d):
    #     if d["status"] == "finished":
    #         print("Done downloading, now converting ...")

    # ydl_opts = {
    #     "format": "bestaudio/best",
    #     "postprocessors": [
    #         {
    #             "key": "FFmpegExtractAudio",
    #             "preferredcodec": "mp3",
    #             "preferredquality": "192",
    #         }
    #     ],
    #     "progress_hooks": [my_hook],
    # }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(["https://www.youtube.com/watch?v=BaW_jenozKc"])


def setup(bot):
    bot.add_cog(_Youtube(bot))
