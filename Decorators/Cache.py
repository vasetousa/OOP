import functools
from pprint import pprint
from time import time


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        if end - start > 0.0:
            print(f'{func.__name__} executed in {end - start} sec >>>')
        return result

    return wrapper


# def cache(func):
#     log = {}
#
#     @functools.wraps(func)
#     def wrapper(num):
#         if num in log:
#             return log[num]
#         log[num] = func(num)
#         return log[num]
#
#     wrapper.log = log
#     return wrapper

""" variant working for ALL functions """


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.keys())
        if cache_key in wrapper.log:
            return wrapper.log[cache_key]
        wrapper.log[cache_key] = func(*args, **kwargs)
        return wrapper.log[cache_key]

    wrapper.log = {}
    return wrapper


@measure_time
@cache
def fibonacci(n):
    print(f'calculating F({n})...')
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(n=100)
# print(fibonacci.log)
# print()
fibonacci(100)
pprint(fibonacci.log)

