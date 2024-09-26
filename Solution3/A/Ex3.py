def gcd_tail(a, b):
    if b == 0:
        return a
    return gcd_tail(b, a % b)

def lcm_tail(a,b):
    return abs(a * b) // gcd_tail(a, b)


print(lcm_tail(12, 15))


def extended_euclidean_recursive(a, b, x0=1, y0=0, x1=0, y1=1):
    if b == 0:
        return a, x0, y0
    else:
        k = a // b
        return extended_euclidean_recursive(b, a % b, x1, y1, x0 - k * x1, y0 - k * y1)


def lcm(a, b):
    return abs(a * b) // extended_euclidean_recursive(a, b)[0]

print(lcm(12,15))
