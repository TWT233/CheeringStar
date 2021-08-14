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
    await client.init_clients()


bot.add_cog(cmd.GroupQuery())
bot.add_cog(cmd.Subscription())

bot.run(conf['bot']['discord'])
