import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def lcp(x,y):
    for i in range(min(len(D[x]),len(D[y]))):
        if D[x][i] != D[y][i]:
            return i
        
    return min(len(D[x]),len(D[y]))

N = int(input())
S = [input() for _ in range(N)]
D = sorted(S)
F = defaultdict(int)

for i in range(N):
    if i == 0:
        F[D[i]] = lcp(i,i+1)
    elif i == N-1:
        F[D[i]] = lcp(i-1,i)
    else:
        F[D[i]] = max(lcp(i-1,i),lcp(i,i+1))

for i in S:
    print(F[i])