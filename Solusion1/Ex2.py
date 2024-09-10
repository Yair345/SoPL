def sum_digit(n):
    return 0 if n == 0 else n % 10 + sum_digit(n // 10)


def sum_digit2(n):
    return sum([int(d) for d in str(n)])


print(sum_digit2(15675867856400))
