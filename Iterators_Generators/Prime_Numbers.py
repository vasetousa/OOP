def is_prime(number):
    return number > 1 and all(number % el for el in range(2, number))


def get_primes(sequence):
    primes = filter(lambda x: is_prime(x), sequence)
    for n in primes:
        yield n



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))