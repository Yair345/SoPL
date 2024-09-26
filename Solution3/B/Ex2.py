import itertools


def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def gen_primes():
    return filter(is_prime, itertools.count(2))


g = gen_primes()
print(list(itertools.islice(g, 5)))
