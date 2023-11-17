import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import (
    accumulate,
    product,
    combinations,
    combinations_with_replacement,
    permutations,
    groupby,
)
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext


def prime_factorize(N):
    D = defaultdict(int)
    if N == 1:
        D[1] += 1
        return D
    i = 2
    while i * i <= N:
        if N % i == 0:
            D[i] += 1
            N //= i
        else:
            i += 1
    if N != 1:
        D[N] += 1

    return D


K = int(input())
tmp = prime_factorize(K)
ans = 0

for key, value in tmp.items():
    if value == 1:
        ans = max(ans, key)
    else:
        for i in range(1, value // 2):
            ans = max(ans, pow(key, i), pow(key, value - i))

print(ans)
