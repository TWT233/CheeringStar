from discord.ext import commands

import doc
from member import get_user_from_id


@commands.command(name='shu_clean')
async def action(ctx: commands.Context):
    print('[cmd] shu_clean {}'.format(ctx.author.name))

    user = get_user_from_id(ctx.author.id)
    if user['permission'] >= 1:
        doc.StatusSheet.shu_clean()
        await ctx.send(ctx.author.mention + ' 樹已經砍掉啦！')
    return
