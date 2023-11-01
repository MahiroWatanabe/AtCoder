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
C = [list(map(int, input().split())) for _ in range(N)]
D = {tuple([0 for _ in range(K)]): 0}

for i in range(N):
    cost, a = C[i][0], C[i][1:]
    old = deepcopy(D)

    for key, val in old.items():
        key = list(key)
        for j in range(K):
            key[j] = min(key[j] + a[j], P)
        key = tuple(key)

        if key in D:
            D[key] = min(D[key], val + cost)
        else:
            D[key] = val + cost

ans = tuple([P for _ in range(K)])

if ans in D:
    print(D[ans])
else:
    print(-1)
