# -*- coding: utf-8 -*-

from discord.ext import commands

import client
import cmd
from config import conf

# init discord bot
description = '''チアリング☆スター：公主连接台服PVP查询Bot，开发&维护：TWT#2333
有BUG/想要新功能的话欢迎PM，但出于各种原因不做侦听排名变动的功能'''

bot = commands.Bot(command_prefix=['!', '！'], description=description, help_command=cmd.MyHelp(),
                   proxy=conf['bot']['proxy'])


@bot.event
async def on_ready():
    print('[ init ] Bot online. Logged in as {} [{}]'.format(bot.user.name, bot.user.id))
    print('[ init ] ------')
    pps = conf['client']['playerprefs']
    for i in range(len(pps)):
        if pps[i]:
            while True:
                try:
                    await client.init_c(i + 1, '../conf/' + pps[i], conf['client']['proxy'])
                except Exception as e:
                    print(e)
                    print(f'[ init ] client {i} init failed')
                    pass
                else:
                    break
    print('[ init ] All clients online.')
    print('[ init ] ------')


bot.add_cog(cmd.GroupQuery())
bot.add_cog(cmd.Subscription())

bot.run(conf['bot']['discord'])
