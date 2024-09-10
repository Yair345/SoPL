def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def get_twin(n):
    return n + 2 if is_prime(n + 2) else n - 2 if is_prime(n - 2) else None


def get_twin_dict(n):
    return {p: get_twin(p) for p in range(n) if is_prime(p) and get_twin(p) is not None}


print(get_twin_dict(50))
