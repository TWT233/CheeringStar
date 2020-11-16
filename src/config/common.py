import json
import os


class Common:
    # filename to config file
    filename: str
    # short of config
    c: dict

    def __init__(self, filename: str):
        Common.filename = os.path.abspath(filename)
        Common.c = json.load(open(filename, 'r', encoding='UTF-8'))

    @staticmethod
    def sync():
        json.dump(Common.c, open(Common.filename, 'w', encoding='UTF-8'), ensure_ascii=False)

    @staticmethod
    def token() -> dict:
        return Common.c['token']

    @staticmethod
    def sheets() -> dict:
        return Common.c['sheets']

    @staticmethod
    def guild() -> dict:
        return Common.c['guild']

    @staticmethod
    def boss() -> dict:
        return Common.c['boss']
