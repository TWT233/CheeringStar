from datetime import datetime
from typing import Tuple, Union

from discord import Embed
from discord.ext import commands
from nowem import PCRAPIException

from client import get_client
from db.crud import bind, get, unbind

_ATTR_NAMES = (('t1_1', '一服1号'), ('t1_2', '一服2号'), ('t2_1', '二服1号'), ('t2_2', '二服2号'),
               ('t3_1', '三服1号'), ('t3_2', '三服2号'), ('t4_1', '四服1号'), ('t4_2', '四服2号'))


class Subscription(commands.Cog, name='速查排名类'):
    """绑定与速查排名"""

    @staticmethod
    def get_bind_embed(did: int) -> Tuple[bool, Union[str, Embed]]:
        now_bind = get(did)

        if not now_bind:
            return False, '尚无绑定记录，请使用[!bind 服务器序号 九位UID]'

        embed = Embed(title=f'当前绑定情况', color=0x4af28a)
        for i in _ATTR_NAMES:
            v = getattr(now_bind[0], i[0])
            if v:
                embed.add_field(name=i[1], value=f"{v}", inline=True)
        embed.set_footer(text='接下来就可以用[!pvp]指令速查排名啦')

        return True, embed

    @commands.command(name='bind', aliases=['綁定', '绑定', 'BIND'])
    async def bind(self, ctx: commands.Context, server_id: int, uid: int):
        """绑定账号，方便查询排名，用法：[!bind 服务器序号 九位UID]，注意空格哦"""
        print(f'[cmd] bind {ctx.author.id} {server_id} {uid}')

        if not get_client(server_id):
            await ctx.send(ctx.author.mention + '不支持当前服务器')
            return

        bind(ctx.author.id, server_id, uid)

        status, res = self.get_bind_embed(ctx.author.id)
        if status:
            await ctx.send(ctx.author.mention, embed=res)
        else:
            await ctx.send(ctx.author.mention + res)
        return

    @commands.command(name='unbind', aliases=['解綁', '解绑', 'UNBIND'])
    async def unbind(self, ctx: commands.Context, server_id: int):
        """解绑账号，用法：[!unbind 服务器序号]，注意空格哦"""
        print(f'[cmd] unbind {ctx.author.id} {server_id}')

        if not get_client(server_id):
            await ctx.send(ctx.author.mention + '不支持当前服务器')
            return

        unbind(ctx.author.id, server_id)

        status, res = self.get_bind_embed(ctx.author.id)
        if status:
            await ctx.send(ctx.author.mention, embed=res)
        else:
            await ctx.send(ctx.author.mention + res)
        return

    @staticmethod
    async def get_pvp_rank(n: int, uid: int) -> str:
        c = get_client(n)
        if not c:
            return '不支持当前服务器'

        try:
            req_result = await c.call.profile.get_profile(int(uid)).exec()
            u = req_result['user_info']

            ret = f'''J: {u['arena_rank']} 名 / P: {u['grand_arena_rank']} 名'''
        except PCRAPIException as e:
            print(e)
            ret = '查询出错，UID错误/机器人故障/游戏服务器维护'
            if e.result_code == 214:
                await c.login()
                ret += '，请重试'

        return ret

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command(name='pvp', aliases=['PVP'])
    async def pvp(self, ctx: commands.Context):
        """双场排名速查，用法：[!pvp]，需要先绑定账号"""
        print(f'[cmd] pvp {ctx.author.id}')

        now_bind = get(ctx.author.id)

        if not now_bind:
            await ctx.send(ctx.author.mention + '尚无绑定记录，输入[!help]查看绑定指令用法')
            return
        entry = now_bind[0]

        try:
            embed = Embed(title=f'速查排名 @ {datetime.now().strftime("%H:%M:%S")}', color=0x4af28a)
            for i in range(len(_ATTR_NAMES)):
                v = getattr(entry, _ATTR_NAMES[i][0])
                if v:
                    res = await self.get_pvp_rank(i // 2 + 1, v)
                    embed.add_field(name=f'{_ATTR_NAMES[i][1]}:{str(v)}', value=f"{res}", inline=True)
            await ctx.send(ctx.author.mention, embed=embed)
            return

        except Exception as e:
            print(e)
            await ctx.send(ctx.author.mention + '查询出错，UID错误/机器人故障/游戏服务器维护')
            return

    @bind.error
    @unbind.error
    @pvp.error
    async def err_uid(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(ctx.author.mention + '服务器序号要用数字表示，uid为连续九位数字。例如：!bind 1 123456789')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.author.mention + '缺少参数哦，检查一下是不是漏了服务器序号。正确例：!bind 1 123456789')

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f'太快啦！请{error.retry_after:.2f}s后再来\n其他命令帮助请看[!help]')
