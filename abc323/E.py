# スライム実装問題
# heapqとdict
# 小さい数字から実装していくので、heapqが適している
# 配列だと10**9の値を持つことができないので、dictで持つ必要がある
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
D = defaultdict(int)
Q = []
heapify(Q)
for _ in range(N):
    S, C = map(int, input().split())
    D[S] = C
    heappush(Q, S)

while Q:
    v = heappop(Q)
    x, y = D[v] // 2, D[v] % 2
    if x >= 1:
        heappush(Q, v * 2)
    D[v * 2] += x
    D[v] = y
cnt = 0
for i, j in D.items():
    cnt += j
print(cnt)
