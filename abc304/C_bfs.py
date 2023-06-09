import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def near(a,b):
    dx = XY[a][0]-XY[b][0]
    dy = XY[a][1]-XY[b][1]
    return dx*dx + dy*dy <= D*D
    
N,D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
Que = deque()
ans = [False for _ in range(N)]
ans[0] = True
Que.append(0)

while Que:
    v = Que.popleft()
    for i in range(N):
        if (near(v,i)):
            if ans[i]:
                continue
            ans[i] = True
            Que.append(i)

for i in range(N):
    if ans[i]:
        print("Yes")
    else:
        print("No")