# heapqは時刻順に取り出すことができる。また、配列を要素として持つことできる
# 計算量の見積もりができてない
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
current = [i for i in range(0,N)]
D = []
heapify(current)
heapify(D)
ans = [0 for _ in range(N)]

for _ in range(M):
    T,W,S = map(int, input().split())
    while len(D) != 0 and D[0][0] <= T:
        v = heappop(D)
        heappush(current,v[1])
    if len(current) != 0:
        v = heappop(current)
        ans[v] += W
        heappush(D,[T+S,v])

for i in ans:
    print(i)