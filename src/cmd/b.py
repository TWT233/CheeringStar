import re

from discord.ext import commands


@commands.command(name='b')
async def __base(ctx: commands.Context, *args):
    count = len(args)

    dmg = ''
    if count >= 1:
        dmg = re.match(r'(\d+)[wW]?(\d+)?', args[0]).groups()
        dmg = int(dmg[1]) * 10000 + (dmg[2] and int(dmg[2]) or 0)

    time = count >= 2 and args[1] or ''

    comments = count >= 3 and args[2] or ''

    represent = count >= 4 and args[3] or ''

    pass
