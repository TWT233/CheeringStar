class AlreadyOnline(Exception):
    def __init__(self, online):
        self.online = online
