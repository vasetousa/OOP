import functools


def some_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass

    return wrapper
