# dfs値戻す
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

def dfs(s,tmp):
    global ans
    visited[s] = True
    ans = max(ans,tmp)

    for to in point[s]:
        if not visited[to] and s != to:
            dfs(to,tmp+dist[s][to])
    visited[s] = False
            
N,M = map(int, input().split())
point = [[] for _ in range(N)]
dist = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A,B,C = map(int, input().split())
    A -= 1
    B -= 1
    point[A].append(B)
    point[B].append(A)
    dist[A][B] = C
    dist[B][A] = C
ans = 0
visited = [False for _ in range(N)]

for i in range(N):
    dfs(i,0)

print(ans)