#!/usr/bin/python

# -*- coding: utf-8 -*-

import json

import discord
from discord.ext import commands

import cmd
import doc
import battle

config = json.load(open('../config/config.json', 'r', encoding='UTF-8'))

# google doc init

doc.StatusSheet('../config/' + config['token']['google'], config['sheets']['key'], config['sheets']['status'])

# battle logger init
battle.Battle(config['boss'], '../config/battle.json')

# discord bot init

description = '''hatsunene'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {} [{}]'.format(bot.user.name, bot.user.id))
    print('------')


bot.add_command(cmd.bd.action)
bot.add_command(cmd.cd.action)
bot.add_command(cmd.shu_clean.action)
bot.add_command(cmd.cc.action)
bot.add_command(cmd.cs.action)
bot.add_command(cmd.ws.action)

bot.run(config['token']['discord'])
