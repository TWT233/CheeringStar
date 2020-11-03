from discord.ext import commands


@commands.command(name='ws')
async def action(ctx: commands.Context):
    print('[cmd] ws {}'.format(ctx.author.name))

    await ctx.send(ctx.guild.get_role(771804609865711636).mention + ' 王死下樹啦！')
    return
