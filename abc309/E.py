import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def bfs(s):
    Que = deque()
    Que.append(s)
    dist = [-1]*N
    dist[s] = 0
    
    while Que:
        v = Que.popleft()
        for nv in point[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                Que.append(nv)
            
    return max(dist),dist.index(max(dist))

N = int(input())
point = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int, input().split())
    A,B = A-1,B-1
    point[A].append(B)
    point[B].append(A)

print(bfs(bfs(0)[1])[0]+1)
