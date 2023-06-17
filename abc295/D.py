import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

S = input()
N = len(S)
x = [[0 for _ in range(10)] for _ in range(N+1)]
ans = 0

for i in range(N):
    c = int(S[i])
    x[i+1] = copy(x[i])
    x[i+1][c] ^= 1

D = defaultdict(int)
for i in x:
    i = tuple(i)
    D[i] += 1

for i,j in D.items():
    ans += j*(j-1)//2

print(ans)