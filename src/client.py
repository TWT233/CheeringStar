import os
from typing import Union, List

from nowem import PCRClient

from config import conf, CONF_DIR

CLIENTS: List[Union[PCRClient, None]] = [None] * 4
VERSION: str = conf['client']['version']


async def init_clients():
    global CLIENTS

    pps = conf['client']['playerprefs']
    for i in range(len(pps)):
        if pps[i]:
            while True:  # remind: infinity retry
                try:
                    CLIENTS[i] = PCRClient(playerprefs=os.path.join(CONF_DIR, pps[i]), proxy=conf['client']['proxy'],
                                           version=get_version())
                    await CLIENTS[i].login()
                except Exception as e:
                    print(e)
                    print(f'[ init ] CLIENTS[{i}] init failed, retrying')
                else:
                    break

    print('[ init ] All clients online.')
    print('[ init ] ------')


def get_client(server_id: int) -> Union[PCRClient, None]:
    if server_id < 1 or server_id > 4:
        raise ValueError(f'unacceptable server_id {server_id}')
    return CLIENTS[server_id - 1]


def get_version():
    return VERSION


def set_version(version: str):
    global VERSION
    VERSION = version
