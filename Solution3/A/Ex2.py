from Ex1 import tuple1000


def sum_recurse(n, t):
    if n == 0:
        return t[0]
    return sum(n - 1) + t[n]


print(sum_recurse(len(tuple1000) - 1, tuple1000))


def sum_tail(n, t):
    def Tsum(n, t, result):
        if n == 0:
            return result + t[0]
        return Tsum(n - 1, t, result + t[n])
    return Tsum(n, t, 0)


print(sum_tail(len(tuple1000) - 1, tuple1000))
