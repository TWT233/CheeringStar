from discord.ext import commands


class MyHelp(commands.DefaultHelpCommand):

    def __init__(self, **options):
        super().__init__(**options)
        self.no_category = '杂项指令'

    def get_ending_note(self):
        return ''
