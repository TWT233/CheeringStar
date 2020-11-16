from discord.ext import commands

from doc import StatusSheet


@commands.command(name='join')
async def action(ctx: commands.Context, *args):
    nickname = len(args) > 0 and args[0] or ctx.author.name

    StatusSheet.add_member(nickname, ctx.author.id)

    await ctx.send('call表填寫成功：{} ({})'.format(ctx.author.name, nickname))

    return
