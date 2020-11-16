import json
import math
import os

from doc import DamageRecord


class Battle:
    boss: dict
    filename: str
    status: dict

    def __init__(self, boss, log_file_name):
        Battle.boss = boss
        Battle.filename = os.path.abspath(log_file_name)
        with open(Battle.filename, 'r', encoding='UTF-8') as f:
            Battle.status = json.load(f)

    @staticmethod
    def current() -> dict:
        return Battle.status['current']

    @staticmethod
    def log() -> list:
        return Battle.status['log']

    @staticmethod
    def sync():
        json.dump(Battle.status, open(Battle.filename, 'w'), ensure_ascii=False, indent=4)

    @staticmethod
    def get_stage(c_round: int):
        if c_round <= 3:
            return 'A'
        elif c_round <= 10:
            return 'B'

    @staticmethod
    def commit(exe: str, dmg: int, rep: str):
        current = Battle.current()
        before = json.dumps({'current': current, 'exe': exe, 'dmg': dmg, 'rep': rep})

        r_time = 0
        real_dmg = dmg

        if current['hp'] <= dmg:
            r_time = min(110 - math.ceil(current['hp'] * 90 / dmg), 90)
            real_dmg = current['hp']
            if current['boss'] == 5:
                current['round'] += 1
                current['boss'] = 1
            else:
                current['boss'] += 1
            current['hp'] = Battle.boss[Battle.get_stage(current['round'])]['hp'][current['boss']]
        else:
            current['hp'] -= dmg

        DamageRecord.commit(current['round'], current['boss'], real_dmg, exe, rep, r_time != 0)
        Battle.log().append(before)
        Battle.sync()

        return r_time

    @staticmethod
    def undo():
        try:
            last_str = Battle.log().pop()
        except IndexError:
            return
        else:
            pass

        last_obj = json.loads(last_str)

        Battle.status['current'] = last_obj['current']
        Battle.sync()

        pass
