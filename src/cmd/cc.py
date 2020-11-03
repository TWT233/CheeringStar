from discord.ext import commands

import doc


@commands.command(name='cc')
async def action(ctx: commands.Context):
    print('[cmd] cc {}'.format(ctx.author.name))

    candao_list = doc.StatusSheet.get_candao()

    ret = "當前殘刀："

    for i in candao_list:
        ret += "\n" + i['name'] + " : " + i['cmt']

    await ctx.send(ctx.author.mention + ret)
    return
