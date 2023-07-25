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


N,M = map(int, input().split())
S = [input() for _ in range(N)]

ans = [[False for _ in range(M)] for _ in range(N)]
ans[1][1] = True

A = set()
XY = [[1,0],[-1,0],[0,1],[0,-1]]
Que = deque()
Que.append([1,1])
A.add((1,1))

while Que:
    x,y = Que.popleft()
    for dx,dy in XY:
        nx,ny = copy(x),copy(y)
        while True:
            nx += dx
            ny += dy
            if S[nx][ny] == ".":
                ans[nx][ny] = True
            else:
                nx -= dx
                ny -= dy
                if (nx,ny) not in A:
                    A.add((nx,ny))
                    Que.append([nx,ny])
                break
cnt = 0
    
for i in range(N):
    for j in range(M):
        if not(i == 0 or i == N-1 or j == 0 or j == M-1) and ans[i][j] == True:
            cnt += 1

print(cnt)