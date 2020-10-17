import json


def get_name_from_id(user_id: int):
    members = json.load(open('../config/config.json', 'r'))['guild']['members']
    for item in members:
        if item['id'] == user_id:
            return item['name']
    return ''


def get_id_from_name(user_name: str):
    members = json.load(open('../config/config.json', 'r'))['guild']['members']
    for item in members:
        if item['name'] == user_name:
            return item['id']
    return ''
