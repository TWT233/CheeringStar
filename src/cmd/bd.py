from discord.ext import commands

from doc import StatusSheet
from exception import MemberNotFound
from member import get_user_from_id, get_user_from_name
from .utils import log


@commands.command(name='bd', aliases=['報', '报'])
@log
async def action(ctx: commands.Context, dmg, cmt, *args):
    rep = len(args) > 0 and args[0] or ''

    try:
        exe = get_user_from_id(ctx.author.id)
        rep_user = get_user_from_name(rep)

        StatusSheet.update_b(exe['name'], dmg, cmt, rep)
        await ctx.send('{} 报刀完成: {} "{}" {}'.format(
            ctx.author.mention, dmg, cmt, ctx.bot.get_user(rep_user['id']).mention))
    except MemberNotFound as e:
        await ctx.send("未找到成员：" + e.expecting)
    finally:
        return


@action.error
async def error_handling(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("参数错误")
