# dp　状態の持ち方が特殊（状態を配列ではなく、dictで持つことで複数の状態を管理している）
# jの要素をdictで持つ
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

N, K, P = map(int, input().split())
D = {tuple([0] * K): 0}

for i in range(N):
    C = list(map(int, input().split()))
    c = C[0]
    a = C[1:]
    old = deepcopy(D)
    for val, key in old.items():
        val = list(val)
        for j in range(K):
            val[j] = min(val[j] + a[j], P)
        val = tuple(val)
        if val in D:
            D[val] = min(D[val], key + c)
        else:
            D[val] = key + c

T = [P for _ in range(K)]
if tuple(T) in D:
    print(D[tuple(T)])
else:
    print(-1)
