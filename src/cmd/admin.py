from discord.ext import commands

from client import get_version, init_clients
from config import conf, save_conf


def is_admin(ctx: commands.Context):
    return ctx.author.id in conf['bot']['admin']


class Admin(commands.Cog, name='管理类'):
    """管理类"""

    @commands.command()
    @commands.check(is_admin)
    async def version(self, ctx: commands.Context, version: str = ''):
        if not version:
            await ctx.reply(f'当前客户端版本：{get_version()}')
            return

        conf['client']['version'] = version
        await save_conf()
        await ctx.reply(f'设置版本号中')
        await init_clients()

    @version.error
    async def err_handler(self, ctx: commands.Context, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.reply('无权限')
