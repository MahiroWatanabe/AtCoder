import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

N,M = map(int, input().split())
P = list(map(int,input().split()))

point = [[] for _ in range(N)]

for i in range(N-1):
    point[P[i]-1].append(i+1)

D = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y += 1
    D[x] = max(D[x], y)

que = deque()
que.append(0)

while que:
    v = que.popleft()
    cost = D[v]
    for ch in point[v]:
        que.append(ch)
        D[ch] = max(D[ch], cost - 1)
        
ans = 0
for i in D:
    if i > 0:
        ans += 1
print(ans)