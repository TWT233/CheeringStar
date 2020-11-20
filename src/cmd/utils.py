import functools


def log(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print('[cmd] ' + ','.join(["\'" + i + "\'" for i in args]))
        return func(*args, **kwargs)

    return wrapper
