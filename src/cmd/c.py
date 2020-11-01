from discord.ext import commands

from battle import *
from doc import *


@commands.command(name='c')
async def action(ctx: commands.Context, *args):
    print('[cmd] c {}'.format(args))

    dmg = len(args) > 0 and args[0] or ''
    rep = len(args) > 1 and args[1] or ''

    remain_time = Battle.commit(dmg)

    if remain_time > 0:
        tree_rip()
