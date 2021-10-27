import functools


def tags(text):
    def str_get(func):
        @functools.wraps(func)
        def wrapper(*args):
            result = func(*args)
            return f'<{text}>{result}</{text}>'

        return wrapper

    return str_get


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
