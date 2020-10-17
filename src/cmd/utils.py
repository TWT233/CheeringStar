import json


def get_name(user_id: int):
    members = json.load(open('../config/config.json', 'r'))['guild']['members']
    for item in members:
        if item['id'] == user_id:
            return item['name']
    return ''
