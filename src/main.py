#!/usr/bin/python

# -*- coding: utf-8 -*-

import discord
import json
from discord.ext import commands

import cmd

# init discord bot
description = '''hatsunene'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['!', '！'],
                   description=description,
                   intents=intents,
                   proxy='http://localhost:7892')


@bot.event
async def on_ready():
    print('[ init ] Bot online. Logged in as {} [{}]'.format(
        bot.user.name, bot.user.id))
    print('[ init ] ------')
    await cmd.cx.init_c(1, '../config/newly.xml', {
        "http": "localhost:7892",
        "https": "localhost:7892"
    })


bot.add_command(cmd.cx.action)

# run
with open('../config/config.json', 'r', encoding='UTF-8') as f:
    bot.run(json.load(f)['bot']['token'])
