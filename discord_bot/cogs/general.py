import discord
import platform
from discord.ext import commands
import datetime
import requests


class _General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #  <---- Writes out if the general.py was loaded correctly ---->
    @commands.Cog.listener()
    async def on_ready(self):
        print("general.py was succesfully loaded!")

    # <---- Writes out if someone joined the server and welcomes him/her ---->
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send("Welcome {0.mention}.".format(member))

    #  <---- Can make a poll ---->
    @commands.command(name="poll")
    async def poll(self, context, *args):
        poll_title = "\n\n".join(args)
        date = f"{context.message.created_at}"
        embed = discord.Embed(
            title=" A new poll has been created!",
            description=f"The title is: {poll_title} \n\nIt was created {date[:-10]}",
            color=0xD75BF4,
        )

        embed.set_footer(text=f"Poll created by: {context.message.author}")

        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    #   <---- kekw meme ---->
    @commands.command(name="kekw")
    async def kekw(self, ctx):
        with open("./0cd.png", "rb") as f:
            picture = discord.File(f)
            meme1 = await ctx.send(file=picture)
            await meme1.add_reaction("👍")


def setup(bot):
    bot.add_cog(_General(bot))