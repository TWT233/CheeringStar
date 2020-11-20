class AlreadyOnline(Exception):
    def __init__(self, who, online):
        self.who = who
        self.online = online
