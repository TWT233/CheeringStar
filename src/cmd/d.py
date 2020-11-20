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
        ret = '誰在代我：'
        for i in d_list['reped']:
            ret += '\n' + i
        ret += '\n我在代誰：'
        for i in d_list['rep']:
            ret += '\n' + i
        await ctx.send('{}{}'.format(ctx.author.mention, ret))
        return

    rep = args[0] or ''
    logout = len(args) >= 2 and args[2] == '下'

    doc.StatusSheet.update_d(exe, rep, logout)
    await ctx.send('{} 代: "{}" {}'.format(
        ctx.author.mention, rep, ctx.bot.get_user(get_user_from_name(rep)['id']).mention))

    return
