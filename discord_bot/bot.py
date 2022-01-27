import discord
from discord.ext import commands
import os
import logging
import asyncio
import random

introduction = """Hello, my name is Python Musk my only purpose is to help you get better! You may guessed it right, yepp im a Python bot. 
I will be online for a couple of hours, when my creator is not doing anything. 
\nIf you see me online you can try the following commands with the prefix of a ' . '(dot):\nbeg \nbeg_sol \nmed \nexp \nguess \nPoll +név +szöveg \nkekw
These are the only commands for now! Have fun"""

hidden_string = "There is nothing here, but hey you have found me! or maybe try $Hello"

bot = commands.Bot(command_prefix=".", description="This is a helper Bot!")


@bot.command()
async def echo(ctx, *, msg: str, description="Vissza adja az értéket"):
    await ctx.send(msg)


@bot.command()
async def whoami(ctx):
    await ctx.send(introduction)


@bot.command()
async def hidden(ctx):
    await ctx.send(hidden_string)


#  <---- When logging on this executes! ---->
@bot.event
async def on_ready():
    print("I am logged on as {0.user}!".format(bot))


#  <---- Simple Mr.Robot reference! ---->
@bot.event
async def on_message(message):
    if message.content.startswith("$hello"):
        channel = message.channel
        await channel.send("Hello Friend! - Elliot Alderson")

        def check(m):
            return m.content == "hello" and m.channel == channel

        message = await bot.wait_for("message", check=check)
        await channel.send("Hello {.author}!".format(message))
    await bot.process_commands(message)


#  <---- Guessing game  ---->
@bot.command()
async def guess(ctx, description="Its a simple guessing game, between 1 - 10"):
    number = random.randint(1, 10)
    await ctx.channel.send("Guess a number between 1 and 10.")
    while True:
        await ctx.channel.send("You can make a guess, now!")
        response = await bot.wait_for(
            "message",
        )
        try:
            guess = int(response.content)
        except ValueError:
            await ctx.channel.send("Give me a number!")
            continue
        if guess > number:
            await ctx.channel.send("The number you guessed is bigger")
        elif guess < number:
            await ctx.channel.send("The number you guessed is smaller")
        else:
            await ctx.channel.send("You are correct {.author}!".format(response))
            return False
    await bot.process_commands(ctx)


#  <---- Can call files from cog folder ---->
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

# <---- Logging everything to .log file ---->
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


bot.run("")
