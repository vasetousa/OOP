import functools


def type_check(t):
    def check_type(func):
        @functools.wraps(t)
        def wrapper(args):
            if type(args) == t:
                return func(args)
            else:
                return "Bad Type"

        return wrapper
    return check_type


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
