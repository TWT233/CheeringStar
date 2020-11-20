import functools


def log(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print('[cmd] ' + args[0].message.content)
        return await func(*args, **kwargs)

    return wrapper
