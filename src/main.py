#!/usr/bin/python

# -*- coding: utf-8 -*-

from discord.ext import commands

import client
import cmd
from config import conf

# init discord bot
description = '''チアリング☆スター：公主连接台服PVP查询Bot
开发&维护：TWT#2333，有BUG/想要新功能的话欢迎PM
但该Bot不会有侦听排名变动的功能哦
觉得好用的话可以请我饮茶或者饮nitro classic'''

bot = commands.Bot(command_prefix=['!', '！'], description=description, help_command=cmd.MyHelp(),
                   proxy=conf['bot']['proxy'])


@bot.event
async def on_ready():
    print('[ init ] Bot online. Logged in as {} [{}]'.format(bot.user.name, bot.user.id))
    print('[ init ] ------')
    pps = conf['client']['playerprefs']
    for i in range(len(pps)):
        if pps[i]:
            await client.init_c(i + 1, '../conf/' + pps[i], conf['client']['proxy'])


bot.add_cog(cmd.GroupQuery())
bot.add_cog(cmd.Subscription())

bot.run(conf['bot']['discord'])
