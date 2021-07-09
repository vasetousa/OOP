from typing import List

class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not any(self.data)

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


s = Stack()
print(s.is_empty())
s.push("100")
s.push("300")
s.push("200")
print(s)
print(s.pop() + '4')
print(s)
print(s.top())
print(s.is_empty())

