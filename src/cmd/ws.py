from discord.ext import commands

import doc


@commands.command(name='ws', aliases=['王死'])
async def action(ctx: commands.Context):
    print('[cmd] ws {}'.format(ctx.author.name))

    doc.StatusSheet.shu_clean()
    await ctx.send(ctx.guild.get_role(771804609865711636).mention + ' 王死下樹啦！')
    return
