from discord.ext import commands

from client import get_c


class GroupQuery(commands.Cog, name='场次查询类指令'):
    """查询PVP场次"""

    async def get_u(self, n: int, uid: int) -> str:
        c = get_c(n)
        if not c:
            return '不支持当前服务器'

        try:
            req_result = await c.call.profile().get_profile(int(uid)).exec()
            u = req_result['user_info']

            ret = (f'''
昵稱：{u['user_name']} ，UID：{u['viewer_id']}，{n}服
JJC場次：{u['arena_group']}，JJC排名：{u['arena_rank']}
PJJC場次：{u['grand_arena_group']}，PJJC排名：{u['grand_arena_rank']}''')
            if u['team_level'] < 187:
                ret += '\n其實是想查其他區？請輸入!help查看其它指令'

        except:
            ret = '查询出错，请检查UID是否正确\n其實是想查其他服？請輸入!help查看其它指令'

        return ret

    @commands.command(name='1cx', aliases=['查詢', '查询', '一区查询', 'CX', 'cx'])
    async def one_cx(self, ctx: commands.Context, uid: int):
        """查询台一PVP场次，用法：[!1cx 九位UID]，注意空格哦"""
        print(f'[cmd] cx {ctx.author.id} {uid}')

        await ctx.send(ctx.author.mention + (await self.get_u(1, uid)))
        return

    @commands.command(name='2cx', aliases=['二區查詢', '二区查询', '2CX'])
    async def two_cx(self, ctx: commands.Context, uid: int):
        """查询台二PVP场次，用法：[!2cx 九位UID]，注意空格哦"""
        print(f'[cmd] 2cx {ctx.author.id} {uid}')

        await ctx.send(ctx.author.mention + (await self.get_u(2, uid)))
        return

    @one_cx.error
    @two_cx.error
    async def err_uid(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(ctx.author.mention + '''UID错误，请输入九位数字UID，UID不需要每三位分隔。例如：!cx 123456789''')
