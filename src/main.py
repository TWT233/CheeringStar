#!/usr/bin/python

# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import cmd
from battle import Battle
from config import Common
from doc import StatusSheet, DamageRecord

# init config
Common('../config/config.json')
print('[ init ] Config loaded. Registered members: {}'.format(len(Common.guild()['members'])))
print('[ init ] ------')

# init battle logger
Battle(Common.c['boss'], '../config/battle.json')
print('[ init ] Battle logger online. Current: {}-{}'.format(Battle.current()['round'], Battle.current()['boss']))
print('[ init ] ------')

# init google doc
StatusSheet('../config/' + Common.token()['google'], Common.sheets()['key'], Common.sheets()['status'])
print('[ init ] Status sheet loaded.')
print('[ init ] ------')
DamageRecord('../config/' + Common.token()['google'], Common.sheets()['key'], Common.sheets()['damage'])
print('[ init ] Damage sheet loaded.')
print('[ init ] ------')

# init discord bot
description = '''hatsunene'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['!', '！'], description=description, intents=intents)


@bot.event
async def on_ready():
    print('[ init ] Bot online. Logged in as {} [{}]'.format(bot.user.name, bot.user.id))
    print('[ init ] ------')


bot.add_command(cmd.bd.action)
bot.add_command(cmd.c.action)
bot.add_command(cmd.cd.action)
bot.add_command(cmd.cc.action)
bot.add_command(cmd.cs.action)
bot.add_command(cmd.jindao.action)
bot.add_command(cmd.jidao.action)
bot.add_command(cmd.join.action)
bot.add_command(cmd.ws.action)
bot.add_command(cmd.shu_clean.action)
bot.add_command(cmd.undo.action)

# run
bot.run(Common.c['token']['discord'])
