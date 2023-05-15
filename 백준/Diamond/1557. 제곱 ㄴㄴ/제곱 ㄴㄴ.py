# import math

def mobius(n):
    if n == 1:
        return 1
    if n % 4 == 0:
        return 0
    square_free = 1
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return 0
        if n % i == 0:
            n //= i
            square_free *= -1
        i += 1
    if n > 1:
        square_free *= -1
    return square_free

def not_Square_num(k):
    lo, hi = 1, 2 * k
    while lo < hi:
        mid = (lo + hi) // 2
        mob = sum(mobius(i) * (mid // (i * i)) for i in range(1, int(mid**0.5) + 1))
        if mob < k:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(not_Square_num(int(input())))