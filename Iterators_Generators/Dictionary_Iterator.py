class dictionary_iter:
    def __init__(self, dict_object):
        self.list_from_dict = list(dict_object.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.list_from_dict):
            raise StopIteration
        idx = self.index
        self.index += 1
        return self.list_from_dict[idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)