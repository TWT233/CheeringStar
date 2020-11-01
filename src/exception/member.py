class MemberNotFound(Exception):
    def __init__(self, arg):
        print('expecting {}'.format(arg))
