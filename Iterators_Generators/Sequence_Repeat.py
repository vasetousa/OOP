class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.lenny = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number:
            raise StopIteration
        value = self.index
        self.index += 1
        return self.sequence[value % self.lenny]



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')