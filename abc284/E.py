import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**9)

def dfs(pos):
    global cnt
    if cnt >= 10**6:
        print(10**6)
        exit()  
    prev[pos] = True
    for nv in point[pos]:
        if prev[nv] == False:
            ans.append(nv)
            cnt += 1
            dfs(nv)
            v = ans.pop()
            prev[v] = False
            
N,M = map(int,input().split())
point = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int, input().split())
    A,B = A-1,B-1
    point[A].append(B)
    point[B].append(A)

prev = [False]*N
ans = [0]
cnt = 1

dfs(0)
print(min(cnt,10**6))