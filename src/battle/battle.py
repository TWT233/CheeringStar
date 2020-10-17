import json
import math
import os


class Battle:
    __instance = None

    def __init__(self, boss, filename):
        self.boss = boss
        self.filename = os.path.abspath(filename)
        with open(self.filename, 'r') as f:
            self.config = json.load(f)
        Battle.__instance = self

    @staticmethod
    def ins():
        return Battle.__instance

    @staticmethod
    def filename():
        return Battle.__instance.filename

    @staticmethod
    def boss():
        return Battle.__instance.config['boss']

    @staticmethod
    def current():
        return Battle.__instance.config['current']

    @staticmethod
    def sync_battle():
        with open(Battle.filename(), 'w') as f:
            json.dump(Battle.ins().config, f)

    @staticmethod
    def get_stage(c_round: int):
        if c_round <= 3:
            return 'A'
        elif c_round <= 10:
            return 'B'

    @staticmethod
    def get_remain_time(dmg: int, c_hp: int):
        return math.ceil(c_hp * 90 / dmg) + 20

    @staticmethod
    def commit(dmg: int):
        current = Battle.current()
        if current['hp'] <= dmg:
            r_time = Battle.get_remain_time(dmg, current['hp'])
            if current['boss'] == 5:
                current['round'] += 1
                current['boss'] = 1
            else:
                current['boss'] += 1
            current['hp'] = Battle.boss()[Battle.get_stage(current['round'])]['hp'][current['boss']]
            return r_time
        else:
            current['hp'] -= dmg
            return 0
