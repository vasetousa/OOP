class Cache:
    def __init__(self, func):
        self.func = func
        self.log = {}

    def __call__(self, args):
        if args in self.log:
            return self.log[args]
        self.log[args] = self.func(args)
        return self.log[args]


@Cache
def fibonacci(n):
    print(f'calculating F({n})...')
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(330)
print(fibonacci.log)