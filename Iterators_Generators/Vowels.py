class vowels:
    def __init__(self, string: str):
        self.string = string
        self.start = 0
        self.vowels_list = ["a", 'o', 'u', 'e', 'i', 'y', 'w']
        self.string_vowels = [x for x in self.string if x.lower() in self.vowels_list]
        self.end = len(self.string_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.string_vowels[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)