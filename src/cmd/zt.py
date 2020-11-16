from discord.ext import commands

from battle import *


@commands.command(name='zt', aliases=['狀態'])
async def action(ctx: commands.Context):
    print('[cmd] zt {}'.format(ctx.author.name))

    await ctx.send(
        '當前進度：{}-{} @ {}'.format(Battle.current()['round'], Battle.current()['boss'], Battle.current()['hp']))
    return
