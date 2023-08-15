import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

def dfs(S):
    ans.append(S)
    seen[S] = True
    
    for to in point[S]:
        if not seen[to]:
            dfs(to)

N = int(input())
point = defaultdict(list)
for _ in range(N):
    A,B = map(int, input().split())
    point[A].append(B)
    point[B].append(A)

ans = []
seen = defaultdict(bool)
dfs(1)

print(max(ans))