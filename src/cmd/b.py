from discord.ext import commands


@commands.command(name='b')
async def action(ctx: commands.Context, *args):
    print('[cmd] .b {}'.format(args))

    dmg = len(args) >= 1 and args[0] or ''

    time = len(args) >= 2 and args[1] or ''

    cmt = len(args) >= 3 and args[2] or ''

    rep = len(args) >= 4 and '@' + args[3] or ''

    await ctx.send('{} [{}] {} {}'.format(dmg, time, cmt, rep))

    pass
