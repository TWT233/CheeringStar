from discord.ext import commands

import doc
from exception import MemberNotFound
from member import get_user_from_id, get_user_from_name


@commands.command(name='c', aliases=['殘'])
async def action(ctx: commands.Context, *args):
    print('[cmd] c {} ({})'.format(ctx.author.name, args))

    cmt = len(args) > 0 and args[0] or ''
    rep = len(args) > 1 and args[1] or ''

    try:
        doc.StatusSheet.update_c(get_user_from_id(ctx.author.id)['name'], cmt, rep)

        await ctx.send('{} 報殘: "{}" {}'.format(
            ctx.author.mention, cmt, rep and ctx.bot.get_user(get_user_from_name(rep)['id']).mention or ''))
    except MemberNotFound:
        return
    else:
        return
