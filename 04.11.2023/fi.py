from math import gcd


def fi(n: int) -> int:
    res = 0
    if n == 1:
        print(1)
        return
    for i in range(1, n):
        if gcd(n, i) == 1:
            res += 1
    print(res)

fi(int(input('N: ')))
input()
