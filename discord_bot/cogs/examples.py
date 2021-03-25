import discord
from discord.ext import commands

question_num_1 = "A nap feladata: Vedd az első 10 számot, és írj egy ismétlődő programot, ami az adott számot össze adja az előzővel"
question_num_2 = "Nincs itt semmi, gyere vissza később!"
question_num_3 = "Itt sincs semmi, gyere vissza később!"

question1_solution = """
def sumNum(num):
    prevNum = 0
    for i in range(num):
        sum = prevNum + i
        print('curr num: ',i, 'prev num: ', prevNum, 'sum: ', sum)
        prevNum = i

sumNum(10)"""


class _Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    # <---- Writes out if example.py was correctly loaded ---->
    @commands.Cog.listener()
    async def on_ready(self):
        print("examples.py was succesfully loaded!")

    @commands.command()
    async def beg(self, ctx, description="A napi kezdő feladat"):
        await ctx.send(question_num_1)

    @commands.command()
    async def med(self, ctx, description="Empty"):
        await ctx.send(question_num_2)

    @commands.command()
    async def exp(self, ctx, description="Empty"):
        await ctx.send(question_num_3)

    @commands.command()
    async def beg_sol(self, ctx, description="A napi kezdő faladat megoldása!"):
        await ctx.send(question1_solution)


def setup(bot):
    bot.add_cog(_Example(bot))