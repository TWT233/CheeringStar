from discord.ext import commands

import doc
from member import get_user_from_id


@commands.command(name='call_clean')
async def action(ctx: commands.Context):
    print('[cmd] call_clean {}'.format(ctx.author.name))

    user = get_user_from_id(ctx.author.id)
    if user['permission'] >= 1:
        doc.StatusSheet.call_clean()
        await ctx.send('call表已清空')
    return
