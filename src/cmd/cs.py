from discord.ext import commands

import doc


@commands.command(name='cs', aliases=['查樹'])
async def action(ctx: commands.Context):
    print('[cmd] cs {}'.format(ctx.author.name))

    shu_list = doc.StatusSheet.get_shu()

    ret = "樹上傷害："

    for i in shu_list:
        ret += "\n" + i['name'] + " : " + i['dmg'] + " : " + i['cmt']

    await ctx.send(ctx.author.mention + ret)
    return
