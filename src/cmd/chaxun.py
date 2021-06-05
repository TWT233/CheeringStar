from typing import Tuple, Union

from discord import Embed
from discord.ext import commands

from client import get_c


class GroupQuery(commands.Cog, name='场次查询类'):
    """查询PVP场次"""

    @staticmethod
    async def get_u(n: int, uid: int) -> Tuple[bool, Union[Embed, str]]:
        c = get_c(n)
        if not c:
            return False, '不支持当前服务器'

        try:
            req_result = await c.call.profile().get_profile(int(uid)).exec()
            u = req_result['user_info']

            embed = Embed(color=0x56b9eb)
            embed.add_field(name='昵稱', value=f"{u['user_name']}", inline=True)
            embed.add_field(name='JJC場次', value=f"{u['arena_group']}", inline=True)
            embed.add_field(name='JJC排名', value=f"{u['arena_rank']}", inline=True)
            embed.add_field(name='UID', value=f"{u['viewer_id']} @ {n}服", inline=True)
            embed.add_field(name='PJJC場次', value=f"{u['grand_arena_group']}", inline=True)
            embed.add_field(name='PJJC排名', value=f"{u['grand_arena_rank']}", inline=True)

            footer = ''
            if u['team_level'] < 187:
                footer += "查錯了服？輸[!help]查看其他服查詢指令"
            footer += '\n新增綁定賬號速查排名功能，輸[!help]了解'
            embed.set_footer(text=footer)

            return True, embed

        except Exception as e:
            print(e)
            return False, '查询出错，UID故障/机器人故障/游戏服务器维护\n輸[!help]查看其他服查询指令'

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command(name='1cx', aliases=['查詢', '查询', '一区查询', 'CX', 'cx'])
    async def one_cx(self, ctx: commands.Context, uid: int):
        """查询台一PVP场次，用法：[!1cx 九位UID]，注意空格哦"""
        print(f'[cmd] cx {ctx.author.id} {uid}')

        status, res = await self.get_u(1, uid)
        if status:
            await ctx.send(ctx.author.mention, embed=res)
        else:
            await ctx.send(ctx.author.mention + res)
        return

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command(name='2cx', aliases=['二區查詢', '二区查询', '2CX'])
    async def two_cx(self, ctx: commands.Context, uid: int):
        """查询台二PVP场次，用法：[!2cx 九位UID]，注意空格哦"""
        print(f'[cmd] 2cx {ctx.author.id} {uid}')

        status, res = await self.get_u(2, uid)
        if status:
            await ctx.send(ctx.author.mention, embed=res)
        else:
            await ctx.send(ctx.author.mention + res)
        return

    @one_cx.error
    @two_cx.error
    async def err_uid(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(ctx.author.mention + '''UID错误，请输入九位数字UID，UID不需要每三位分隔。例如：!1cx 123456789''')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.author.mention + '缺少参数哦，检查一下是不是漏了uid。正确例：!1cx 123456789')

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(ctx.author.mention + '两分钟内仅可查询一次，请稍后再来')
