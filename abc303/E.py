import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

def dfs(v,p,d):
    if d%3 == 1:
        ans.append(len(point[v]))
    for to in point[v]:
        if to != p:
            dfs(to,v,d+1)

N = int(input())
point = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    point[a].append(b)
    point[b].append(a)
ans = []

leaf = -1
for i in range(N):
    if len(point[i]) == 1:
        leaf = i

dfs(leaf,-1,0)

ans.sort()
print(*ans)