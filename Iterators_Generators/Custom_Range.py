class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp_value = self.start
        self.start += 1
        return temp_value


for el in custom_range(0, 70):
    print(el, end=" ")
