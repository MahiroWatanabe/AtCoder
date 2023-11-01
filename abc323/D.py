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

N = int(input())
SC = sorted([list(map(int, input().split())) for _ in range(N)])
D = defaultdict(int)
for i in range(N):
    D[SC[i][0]] = SC[i][1]
index = 0

while len(SC) != index:
    print(SC[index])
    D[SC[index][0] * 2] += SC[index][1] // 2
    D[SC[index][0]] -= SC[index][1] // 2 * 2
    index += 1
    print(D)

cnt = 0
for i, j in D.items():
    cnt += j
print(cnt)
