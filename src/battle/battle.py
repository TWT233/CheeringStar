import json
import math
import os


class Battle:
    boss: dict
    filename: str
    config: dict
    log: list

    def __init__(self, boss, log_file_name):
        Battle.boss = boss
        Battle.filename = os.path.abspath(log_file_name)
        Battle.log = []
        with open(Battle.filename, 'r', encoding='UTF-8') as f:
            Battle.config = json.load(f)

    @staticmethod
    def current() -> dict:
        return Battle.config['current']

    @staticmethod
    def sync_battle():
        with open(Battle.filename, 'w') as f:
            json.dump(Battle.config, f)

    @staticmethod
    def get_stage(c_round: int):
        if c_round <= 3:
            return 'A'
        elif c_round <= 10:
            return 'B'

    @staticmethod
    def commit(dmg: int):
        current = Battle.current()
        r_time = 0

        before = json.dumps(current)

        if current['hp'] <= dmg:
            r_time = min(110 - math.ceil(current['hp'] * 90 / dmg), 90)
            if current['boss'] == 5:
                current['round'] += 1
                current['boss'] = 1
            else:
                current['boss'] += 1
            current['hp'] = Battle.boss[Battle.get_stage(current['round'])]['hp'][current['boss']]
        else:
            current['hp'] -= dmg

        Battle.log.append(before)

        return r_time

    @staticmethod
    def undo():
        try:
            last = Battle.log.pop()
        except IndexError:
            return
        else:
            pass

        Battle.config['current'] = json.loads(last)
        pass
