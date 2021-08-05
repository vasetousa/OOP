class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.count:
            raise StopIteration
        value = self.start
        self.start += 1
        return value * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)