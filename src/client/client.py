from typing import Union
from nowem import PCRClient

c = [None] * 4
inited = [False] * 4


async def init_c(server: int, ppfile: str, proxy: dict = {}):
    server -= 1
    global c
    c[server] = PCRClient(playerprefs=ppfile, proxy=proxy)
    await c[server].login()
    inited[server] = True


def get_c(server: int) -> Union[PCRClient, None]:
    server -= 1
    if inited[server]:
        return c[server]
    else:
        return None
