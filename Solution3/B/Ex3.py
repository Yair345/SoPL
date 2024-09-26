import math
from itertools import accumulate, count


def power_function(num):
    return lambda x: x ** num


power_of_2 = power_function(2)


def power_map(num):
    return map(power_function, count(num))


def taylor_approximation(x):
    return (func(x) / math.factorial(i) for i, func in enumerate(power_map(0)))


def taylor_series_generator(x):
    return accumulate(taylor_approximation(x))


generator = taylor_series_generator(2)

for _, approximation in zip(range(8), generator):
    print(f"{approximation:.15f}")
