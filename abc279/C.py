import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

H,W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
SD = defaultdict(int)
TD = defaultdict(int)

for j in range(W):
    N = ""
    for i in range(H):
        N += S[i][j]
    SD[N] += 1
    
for j in range(W):
    N = ""
    for i in range(H):
        N += T[i][j]
    TD[N] += 1

for key,value in SD.items():
    if value != TD[key]:
        print("No")
        exit()

print("Yes")