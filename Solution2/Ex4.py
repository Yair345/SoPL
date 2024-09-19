import math


def power_function(num):
    return lambda x: x ** num


power_of_2 = power_function(2)
print(power_of_2(5))


def power_map(num):
    return map(power_function, range(num))


print(list(power_map(5))[3](5))


def taylor_approximation(x, n):
    return sum([func(x) / math.factorial(i) for i, func in enumerate(power_map(n))])


print(taylor_approximation(1, 20))
