# 帰りがけ順
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

def dfs(s):
    visited[s] = True
    if len(point[s]) == 0:
        return
    
    for to in point[s]:
        if not visited[to] and s != to:
            dfs(to)
            ans.append(to+1)

N = int(input())
point = [[] for _ in range(N)]
for i in range(N):
    C,*P = map(int, input().split())
    for j in P:
        point[i].append(j-1)
ans = []
visited = [False for _ in range(N)]

dfs(0)

print(*ans)