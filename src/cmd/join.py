from discord.ext import commands

from doc import StatusSheet


@commands.command(name='join')
async def action(ctx: commands.Context, *args):

    nickname = len(args) > 0 and args[0] or ctx.author.name

    StatusSheet.add_member(nickname)

    await ctx.send('call表填寫成功：{} ({})'.format(ctx.author.name, nickname))

    print('{"name": "'+nickname+'","id": '+str(ctx.author.id)+',"permission": 0},')
    return
