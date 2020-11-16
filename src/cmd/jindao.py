from discord.ext import commands

from doc import StatusSheet
from member import get_user_from_id


@commands.command(name='jindao', aliases=['進'])
async def action(ctx: commands.Context, *args):
    print('[cmd] jindao {}'.format(ctx.author.name))

    rep = len(args) > 0 and args[0] or ''

    StatusSheet.update_jd(get_user_from_id(ctx.author.id)['name'], rep, True)

    await ctx.send('{}進刀成功'.format(ctx.author.mention))
    return
