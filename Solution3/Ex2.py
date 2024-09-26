from Ex1 import tuple1000


def sum(n):
    if n == 0:
        return tuple1000[0]
    return sum(n - 1) + tuple1000[n]


print(sum(len(tuple1000) - 1))


def sum_tail(n):
    def Tsum(n, result):
        if n == 0:
            return result + tuple1000[0]
        return Tsum(n - 1, result + tuple1000[n])
    return Tsum(n, 0)


print(sum_tail(len(tuple1000) - 1))
