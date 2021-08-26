import os
from typing import Union, List

from nowem import PCRClient

from config import conf, CONF_DIR

CLIENTS: List[Union[PCRClient, None]] = [None] * 4


async def init_clients():
    global CLIENTS

    pps = conf['client']['playerprefs']
    for i in range(len(pps)):
        if not pps[i]:
            continue
        for retry_times in range(max_retry_times()):
            c = PCRClient(playerprefs=os.path.join(CONF_DIR, pps[i]), proxy=conf['client']['proxy'],
                          version=get_version())
            try:
                await c.login()
            except Exception as e:
                print(e)
                print(f'[ init ] CLIENTS[{i}] init failed, retrying {retry_times + 1}')
            else:
                CLIENTS[i] = c
                break

    print('[ init ] Clients inited.')
    print('[ init ] ------')


def get_client(server_id: int) -> Union[PCRClient, None]:
    if server_id < 1 or server_id > 4:
        raise ValueError(f'unacceptable server_id {server_id}')
    return CLIENTS[server_id - 1]


def get_version():
    return conf['client']['version']


def max_retry_times():
    return conf['client']['max_retry_times']
