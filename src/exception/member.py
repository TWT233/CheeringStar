class MemberNotFound(Exception):
    def __init__(self, expecting):
        self.expecting: str = expecting
        print('MemberNotFound: {}'.format(expecting))
