class MemberNotFound(Exception):
    def __init__(self, expecting):
        self.expecting: str = str(expecting)
