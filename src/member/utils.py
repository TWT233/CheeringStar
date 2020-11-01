import json

from exception import MemberNotFound

members = json.load(open('../config/config.json', 'r', encoding='UTF-8'))['guild']['members']


def get_user_from_id(user_id: int):
    for item in members:
        if item['id'] == user_id:
            return item
    print('get_user_from_id failed')
    raise MemberNotFound(user_id)


def get_user_from_name(user_name: str):
    for item in members:
        if item['name'] == user_name:
            return item
    print('get_user_from_name failed')
    raise MemberNotFound(user_name)
