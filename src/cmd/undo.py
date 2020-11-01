from discord.ext import commands

from battle import *
from member import get_user_from_id


@commands.command(name='undo')
async def action(ctx: commands.Context):
    print('[cmd] undo {}'.format(ctx.author.name))

    user = get_user_from_id(ctx.author.id)
    if user['permission'] >= 1:
        Battle.undo()
        current = Battle.current()
        await ctx.send('当前进度: {}@{}-{}'.format(current['hp'], current['round'], current['boss']))

    return
