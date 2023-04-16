import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

Q = int(input())
MOD = 998244353
q = deque()
q.append(1)
r = 1

for _ in range(Q):
    s = list(map(int,input().split()))
    if s[0] == 1:
        x = s[1]
        q.append(x)
        r = (r * 10 + x) % MOD
    elif s[0] == 2:
        y = q.popleft()
        r = (r - y*pow(10,len(q),MOD)) % MOD
    else:
        print(r)