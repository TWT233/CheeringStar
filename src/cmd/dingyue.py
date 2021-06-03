from datetime import datetime

from discord import Embed
from discord.ext import commands

from client import get_c
from db.crud import bind, get, unbind


class Subscription(commands.Cog):
    """绑定与快速查询排名"""

    @commands.command(name='bind', aliases=['綁定', '绑定'])
    async def bind(self, ctx: commands.Context, server_id: int, uid: int):
        """绑定账号，方便查询排名，用法：[!bind 服务器序号 九位UID]，注意空格哦"""
        print(f'[cmd] bind {ctx.author.id} {server_id} {uid}')

        if not get_c(server_id):
            await ctx.send(ctx.author.mention + '不支持当前服务器')
            return

        bind(ctx.author.id, server_id, uid)
        now_bind = get(ctx.author.id)

        embed = Embed(title=f'当前绑定情况')
        embed.add_field(name='一服1号', value=f"{now_bind[0].t1_1 or '空'}", inline=True)
        embed.add_field(name='一服2号', value=f"{now_bind[0].t1_2 or '空'}", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='二服1号', value=f"{now_bind[0].t2_1 or '空'}", inline=True)
        embed.add_field(name='二服2号', value=f"{now_bind[0].t2_2 or '空'}", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        await ctx.send(ctx.author.mention, embed=embed)
        return

    @commands.command(name='unbind', aliases=['解綁', '解绑'])
    async def unbind(self, ctx: commands.Context, server_id: int):
        """解绑账号，用法：[!unbind 服务器序号]，注意空格哦"""
        print(f'[cmd] unbind {ctx.author.id} {server_id}')

        if not get_c(server_id):
            await ctx.send(ctx.author.mention + '不支持当前服务器')
            return

        unbind(ctx.author.id, server_id)
        now_bind = get(ctx.author.id)

        embed = Embed(title=f'当前绑定情况')
        embed.add_field(name='一服1号', value=f"{now_bind[0].t1_1 or '空'}", inline=True)
        embed.add_field(name='一服2号', value=f"{now_bind[0].t1_2 or '空'}", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='二服1号', value=f"{now_bind[0].t2_1 or '空'}", inline=True)
        embed.add_field(name='二服2号', value=f"{now_bind[0].t2_2 or '空'}", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        await ctx.send(ctx.author.mention, embed=embed)
        return

    @staticmethod
    async def get_u(n: int, uid: int) -> str:
        c = get_c(n)
        if not c:
            return '不支持当前服务器'

        try:
            req_result = await c.call.profile().get_profile(int(uid)).exec()
            u = req_result['user_info']

            ret = f'''J:{u['arena_rank']}/P:{u['grand_arena_rank']}'''
        except:
            ret = '查询出错，请检查UID'

        return ret

    @commands.command(name='pvp')
    async def pvp(self, ctx: commands.Context):
        """快速查询pvp排名，用法：[!pvp]，需要先绑定账号"""
        print(f'[cmd] pvp {ctx.author.id}')

        now_bind = get(ctx.author.id)

        if not now_bind:
            await ctx.send(ctx.author.mention + '尚无绑定记录，请使用[!bind 服务器序号 九位UID]')
            return


        try:
            embed = Embed(title=f'速查排名@{datetime.now().strftime("%H:%M:%S")}')
            if now_bind[0].t1_1:
                uid = now_bind[0].t1_1
                res = await self.get_u(1, uid)
                embed.add_field(name='一服1号：' + str(uid), value=f"{res}", inline=True)
            if now_bind[0].t1_2:
                uid = now_bind[0].t1_2
                res = await self.get_u(1, uid)
                embed.add_field(name='一服2号：' + str(uid), value=f"{res}", inline=True)
            if now_bind[0].t2_1:
                uid = now_bind[0].t2_1
                res = await self.get_u(2, uid)
                embed.add_field(name='二服1号：' + str(uid), value=f"{res}", inline=True)
            if now_bind[0].t2_2:
                uid = now_bind[0].t2_2
                res = await self.get_u(2, uid)
                embed.add_field(name='二服2号：' + str(uid), value=f"{res}", inline=True)
            await ctx.send(ctx.author.mention, embed=embed)
            return

        except Exception as e:
            print(e)
            await ctx.send(ctx.author.mention + '查询出错，UID故障/机器人故障/游戏服务器维护')
            return
