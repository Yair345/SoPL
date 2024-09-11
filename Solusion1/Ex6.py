def time_two(n):
    return 2 * n


def square(n):
    return n ** 2


def negative(n):
    return -1 * n


def apply_functions(numbers, functions):
    return {func.__name__: tuple([func(num) for num in numbers]) for func in functions}


print(apply_functions(range(1, 10), (time_two, square, negative)))
