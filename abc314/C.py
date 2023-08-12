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
S = input()
C = list(map(int,input().split()))
D = defaultdict(int)
ans = ""

color_positions = [[] for _ in range(M)]
for i in range(N):
    D[i] = len(color_positions[C[i]-1])
    color_positions[C[i] - 1].append(i)

for i in range(N):
    ans += S[color_positions[C[i]-1][(D[i]-1)%len(color_positions[C[i]-1])]]
    
print(ans)