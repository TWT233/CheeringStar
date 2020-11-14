from discord.ext import commands

import doc
from battle import *


@commands.command(name='cd', aliases=['出'])
async def action(ctx: commands.Context, *args):
    print('[cmd] cd {} {}'.format(ctx.author.name, args))

    dmg = len(args) > 0 and args[0] or ''
    rep = len(args) > 1 and args[1] or ''

    remain_time = Battle.commit(int(dmg))

    if remain_time > 0:
        doc.StatusSheet.shu_clean()

    current = Battle.current()

    await ctx.send(
        '{} 出刀完成: {} {} {}\n当前进度: {}@{}-{}'.format(ctx.author.mention, dmg,
                                                   remain_time and '返' + str(remain_time) + 's' or '',
                                                   rep, current['hp'], current['round'], current['boss']))
    return
