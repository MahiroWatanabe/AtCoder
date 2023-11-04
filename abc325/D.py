# スケジューリング問題　左でソートして右の最小を取っていく　heapq
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
TD = []
for _ in range(N):
    T, D = map(int, input().split())
    TD.append([T, T + D])
TD.sort()
ans = 0

que = []
heapify(que)
t = 0
index = 0

while index < N or que:
    while index < N and TD[index][0] <= t:
        heappush(que, TD[index][1])
        index += 1

    while que and que[0] < t:
        heappop(que)

    if que:
        ans += 1
        heappop(que)

    if not que and index < N:
        t = TD[index][0]
    else:
        t += 1

print(ans)
