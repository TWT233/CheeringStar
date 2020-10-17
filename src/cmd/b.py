from discord.ext import commands

from doc import StatusSheet

from .utils import get_name


@commands.command(name='b')
async def action(ctx: commands.Context, *args):
    print('[cmd] .b {}'.format(args))

    dmg = len(args) >= 1 and args[0] or ''

    time = len(args) >= 2 and args[1] or ''

    cmt = len(args) >= 3 and args[2] or ''

    rep = len(args) >= 4 and args[3] or ''

    StatusSheet.update_b(get_name(ctx.author.id), dmg, time, cmt, rep)

    await ctx.send('{} 报刀完成: {} [{}] {} {}'.format(ctx.author.mention, dmg, time, cmt, rep))

    pass
