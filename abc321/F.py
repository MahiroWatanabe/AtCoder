# heapqは時刻順に取り出すことができる。また、配列を要素として取ることもできる
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
ans = [0 for _ in range(N+1)]
current = []
for i in range(1,N+1):
    heappush(current,i)
heapify(current)
D = defaultdict(int)

for _ in range(M):
    T,W,S = map(int, input().split())
    if D[T] != 0:
        heappush(current,D[T])
    if len(current) > 0:
        v = heappop(current)
        D[T+S] = v
        ans[v] += W

for i in ans[1:]:
    print(i)