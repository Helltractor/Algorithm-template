ImportType = 1
InputType = 1
ConstType = 1
if ImportType:
    import os, sys, random, threading
    from random import randint, choice, shuffle
    from copy import deepcopy
    from io import BytesIO, IOBase
    from types import GeneratorType
    from functools import lru_cache, reduce
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush, heappushpop
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, comb, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    from decimal import Decimal, getcontext
    from sys import stdin, stdout, setrecursionlimit

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    I = lambda: input()
    II = lambda: int(input())
    MII = lambda: map(int, input().split())
    LI = lambda: list(input().split())
    LII = lambda: list(map(int, input().split()))
    GMI = lambda: map(lambda x: int(x) - 1, input().split())
    LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353
    Y = "Yes"
    N = "No"

# 1 | 2, 1 | 2 | 3, 2 | 3 | 4
# 1 | 2 | 3, 1 | 2 | 3 | 4, 1 | 2 | 3 | 4 | 5
def cf_B():
    for _ in range(II()):
        n, m = MII()
        ans = 0
        l, r = max(n - m, 0), n + m
        for i in range(64):
            if ((l >> i) & 1) | ((r >> i) & 1):
                ans |= (1 << i)
            elif l + (1 << i) <= r:
                ans |= 1 << i
        print(ans)
    return


def main():
    cf_B()
    # tmp = list(range(32))
    # for _ in range(8):
    #     a = tmp.copy()
    #     for i in range(len(tmp)):
    #         if i == 0:
    #             tmp[i] |= a[i + 1]
    #         elif i + 1 < len(tmp):
    #             tmp[i] |= a[i - 1] | a[i + 1]
    #         else:
    #             tmp[i] |= a[i - 1]
    #     print(tmp)
        
    return


if __name__ == '__main__':
    main()
