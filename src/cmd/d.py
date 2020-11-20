from discord.ext import commands

import doc
from exception import MemberNotFound
from member import get_user_from_id, get_user_from_name


@commands.command(name='d', aliases=['代'])
async def action(ctx: commands.Context, *args):
    print('[cmd] d {} ({})'.format(ctx.author.name, args))

    try:
        exe = get_user_from_id(ctx.author.id)['name']
    except MemberNotFound:
        return

    if len(args) == 0:
        d_list = doc.StatusSheet.get_d(exe)
        ret = '誰在代我：' + '\n'.join(d_list['reped'])
        ret += '\n我在代誰：' + '\n'.join(d_list['rep'])
        await ctx.send('{}\n{}'.format(ctx.author.mention, ret))
        return

    rep = args[0] or ''
    logout = len(args) >= 2 and args[1] == '下'

    doc.StatusSheet.update_d(exe, rep, logout)
    await ctx.send('{} {}: {} {}'.format(
        ctx.author.mention, logout and '下' or '代', rep, ctx.bot.get_user(get_user_from_name(rep)['id']).mention))

    return
