def get_pentaNum(n: int) -> int:
    return (n * (3 * n - 1)) // 2


def penta_num_range(n1: int, n2: int):
    return [get_pentaNum(n) for n in range(n1, n2)]


print(penta_num_range(3,8))
