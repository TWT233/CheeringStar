import json


def get_user_from_id(user_id: int):
    members = json.load(open('../config/config.json', 'r'))['guild']['members']
    for item in members:
        if item['id'] == user_id:
            return item
    return {}


def get_user_from_name(user_name: str):
    members = json.load(open('../config/config.json', 'r'))['guild']['members']
    for item in members:
        if item['name'] == user_name:
            return item
    return {}
