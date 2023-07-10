import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def bfs(s):
    Que = deque()
    Que.append(s)
    dist = [-1 for _ in range(N1+N2)]
    dist[s] = 0
    
    while Que:
        v = Que.popleft()
        for to in point[v]:
            if dist[to] == -1:
                dist[to] = dist[v]+1
                Que.append(to)
                
    return max(dist)

N1,N2,M = map(int, input().split())
point = [[] for _ in range(N1+N2)]
for _ in range(M):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    point[a].append(b)
    point[b].append(a)

x = bfs(0)
y = bfs(N1+N2-1)
print(x+y+1)