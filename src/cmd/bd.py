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

        StatusSheet.update_b(exe['name'], dmg, cmt, rep)
        await ctx.send('{} 报刀完成: {} "{}" {}'.format(
            ctx.author.mention, dmg, cmt, rep and ctx.bot.get_user(get_user_from_name(rep)['id']).mention or ''))

    except MemberNotFound as e:
        await ctx.send("找不到成員：" + e.expecting)
    finally:
        return


@action.error
async def error_handling(ctx: commands.Context):
    await ctx.send("{} 指令解析遇到錯誤啦，請重新檢查".format(ctx.author.mention))
