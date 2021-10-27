import functools
import time


def exec_time(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return end - start
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 100000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


