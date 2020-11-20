class ArgumentNotEnough(Exception):
    def __init__(self, exact, excepting):
        self.exact = exact
        self.excepting = excepting
