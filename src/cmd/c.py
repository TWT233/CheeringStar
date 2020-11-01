from discord.ext import commands

from battle import *
from doc import *
from member import get_user_from_id


@commands.command(name='c')
async def action(ctx: commands.Context, *args):
    print('[cmd] c {} {}'.format(ctx.author.name, args))

    dmg = len(args) > 0 and args[0] or ''
    rep = len(args) > 1 and args[1] or ''

    remain_time = Battle.commit(dmg)

    if remain_time > 0:
        doc.StatusSheet.call_clean()

    current = Battle.current()

    await ctx.send(
        '{} 出刀完成: {} {} {}\n当前进度: {}@{}-{}'.format(ctx.author.mention, dmg,
                                                   remain_time and '返' + str(remain_time) + 's' or '',
                                                   rep, current['hp'], current['round'], current['boss']))
    return
