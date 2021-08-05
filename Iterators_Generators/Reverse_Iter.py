class reverse_iter:
    def __init__(self, list_obj):
        self.list_obj = list_obj
        self.start = len(list_obj) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
        temp_value = self.start
        self.start -= 1
        return self.list_obj[temp_value]




reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)