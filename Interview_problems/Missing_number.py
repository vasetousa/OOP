""" missing number,  find it (10) """
from random import randint

start = 1
end = 20
string = set([int(y) for y in input().split(', ')])

''' generate a range from 1 to N+1 '''
l = []
[l.append(x) for x in range(start, end)]
l = set(l)

missing_number = l.difference(string)
print(*missing_number)

# input numbers with missing '10' ->> 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20