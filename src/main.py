# This example requires the 'members' privileged intents
import json

import discord
from discord.ext import commands

from .cmd import b

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

token = json.load(open('../config/config.json', 'r'))['bot']['token']

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {} [{}]'.format(bot.user.name, bot.user.id))
    print('------')


bot.add_command(b.__base)

bot.run(token)
