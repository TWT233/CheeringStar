from discord.ext import commands

from client import get_c


class GroupQuery(commands.Cog,name='场次查询类指令'):
    """查询PVP场次"""

    @commands.command(name='1cx', aliases=['查詢', '查询', '一区查询', 'CX', 'cx'])
    async def cx(self, ctx: commands.Context, uid: int):
        """查询台一PVP场次，用法：[!1cx 九位UID]，注意空格哦"""

        print(f'[cmd] cx {ctx.author.id} {uid}')

        c = get_c(1)
        if not c:
            await ctx.send(ctx.author.mention + '不支持当前服务器')
            return

        try:
            req_result = await c.call.profile().get_profile(int(uid)).exec()
            u = req_result['user_info']

            ret = (f'''
昵稱：{u['user_name']} ，UID：{u['viewer_id']}，一區
JJC場次：{u['arena_group']}，JJC排名：{u['arena_rank']}
PJJC場次：{u['grand_arena_group']}，PJJC排名：{u['grand_arena_rank']}''')
            if u['team_level'] < 187:
                ret += '\n其實是想查其他區？請輸入!help查看其它指令'

        except:
            ret = '查询出错，请检查UID是否正确'

        await ctx.send(ctx.author.mention + ret)
        return

    @commands.command(name='2cx', aliases=['二區查詢', '二区查询', '2CX'])
    async def twocx(self, ctx: commands.Context, uid: int):
        """查询台二PVP场次，用法：[!2cx 九位UID]，注意空格哦"""

        print(f'[cmd] 2cx {ctx.author.id} {uid}')

        c = get_c(2)
        if not c:
            await ctx.send(ctx.author.mention + '不支持当前服务器')
            return

        try:
            req_result = await c.call.profile().get_profile(int(uid)).exec()
            u = req_result['user_info']

            ret = (f'''
昵稱：{u['user_name']} ，UID：{u['viewer_id']}，二區
JJC場次：{u['arena_group']}，JJC排名：{u['arena_rank']}
PJJC場次：{u['grand_arena_group']}，PJJC排名：{u['grand_arena_rank']}''')
            if u['team_level'] < 187:
                ret += '\n其實是想查其他區？請輸入!help查看其它指令'

        except:
            ret = '查询出错，请检查UID是否正确'

        await ctx.send(ctx.author.mention + ret)
        return

    @cx.error
    @twocx.error
    async def err_uid(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(ctx.author.mention + '''UID错误，请输入九位数字UID，UID不需要每三位分隔。
    例如：!cx 123456789''')
