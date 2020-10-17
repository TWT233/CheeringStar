from discord.ext import commands

from doc import StatusSheet

from member import get_name_from_id, get_id_from_name


@commands.command(name='b')
async def action(ctx: commands.Context, *args):
    print('[cmd] .b {}'.format(args))

    dmg = len(args) > 0 and args[0] or ''

    cmt = len(args) > 1 and args[1] or ''

    rep = len(args) > 2 and args[2] or ''

    StatusSheet.update_b(get_name_from_id(ctx.author.id), dmg, cmt, rep)

    mention_rep = ctx.bot.get_user(get_id_from_name(rep)).mention

    await ctx.send('{} 报刀完成: {} "{}" {}'.format(ctx.author.mention, dmg, cmt, rep and mention_rep or ''))

    pass
