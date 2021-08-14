import os

from discord.ext import commands
from nowem import PCRClient

from client import get_version, init_clients
from config import conf, CONF_DIR, save_conf


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

        pps = conf['client']['playerprefs']
        for i in range(len(pps)):
            if pps[i]:
                try:
                    c = PCRClient(playerprefs=os.path.join(CONF_DIR, pps[i]),
                                  proxy=conf['client']['proxy'],
                                  version=version)
                    await c.login()
                except Exception as e:
                    print(e)
                    print(f'version check failed')
                    await ctx.reply(f'该版本号不可用')
                else:
                    conf['client']['version'] = version
                    await save_conf()
                    await ctx.reply(f'该版本号可用，设置中')
                break
        await init_clients()

    @version.error
    async def err_handler(self, ctx: commands.Context, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.reply('无权限')
