class ArgumentNotEnough(Exception):
    def __init__(self, exact, excepting):
        print('ArgumentNotEnough: got {}, expecting {}'.format(exact, excepting))
