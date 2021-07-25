from discord.ext import commands


class MyHelp(commands.DefaultHelpCommand):

    def __init__(self, **options):
        super().__init__(**options)
        self.no_category = '杂项指令'

    def get_ending_note(self):
        return '觉得好用的话可以请我饮茶或者饮nitro classic\n本Bot邀请链接：https://bit.ly/3uKyPeX，朋友想用的话欢迎转邀'
