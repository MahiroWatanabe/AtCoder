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

def c2(n):
    return n*(n-1)//2

def dfs(index,ns):
    colors[index] = ns
    csv[ns] += 1
    for to in point[index]:
        if colors[to] == ns:
            return False
        if colors[to] == -1 and not dfs(to,0 if ns == 1 else 1):
            return False
        
    return True

N,M = map(int, input().split())
point = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    point[u].append(v)
    point[v].append(u)

ans = c2(N)-M
colors = [-1 for _ in range(N)]

for i in range(N):
    if colors[i] != -1:
        continue
    
    csv = [0 for _ in range(2)]
    
    if not dfs(i,1):
        print(0)
        exit()
    
    for i in range(2):
        ans -= c2(csv[i])

print(ans)