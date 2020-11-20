from discord.ext import commands

from doc import StatusSheet
from exception import MemberNotFound
from member import get_user_from_id, get_user_from_name


@commands.command(name='bd', aliases=['報'])
async def action(ctx: commands.Context, *args):
    print('[cmd] bd {} {}'.format(ctx.author.name, args))

    dmg = len(args) > 0 and args[0] or ''
    cmt = len(args) > 1 and args[1] or ''
    rep = len(args) > 2 and args[2] or ''

    try:
        StatusSheet.update_b(get_user_from_id(ctx.author.id)['name'], dmg, cmt, rep)

        await ctx.send('{} 报刀完成: {} "{}" {}'.format(ctx.author.mention, dmg, cmt,
                                                    rep and ctx.bot.get_user(
                                                        get_user_from_name(rep)['id']).mention or ''))
    except MemberNotFound:
        return


@action.error
async def error_handling(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("参数错误")
