from itertools import permutations


def possible_permutations(sequence):
    return (list(per) for per in permutations(sequence))


[print(n) for n in possible_permutations([1, 2, 3])]