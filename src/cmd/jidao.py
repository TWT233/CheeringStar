from discord.ext import commands


@commands.command(name='jidao', aliases=['集刀'])
async def action(ctx: commands.Context):
    print('[cmd] jidao {}'.format(ctx.author.name))

    await ctx.send('集刀！{}\n'.format(ctx.guild.get_role(771804609865711636).mention))
    return
