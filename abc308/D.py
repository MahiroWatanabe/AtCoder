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

def dfs(sx,sy,cnt):    
    for dx,dy in XY:
        x,y = sx+dx,sy+dy
        if 0 <= x < H and 0 <= y < W and not dist[x][y]:
            if S[x][y] == E[(cnt+1)%5]:
                if x == H-1 and y == W-1:
                    print("Yes")
                    exit()
                dist[x][y] = True
                dfs(x,y,cnt+1)

H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
E = "snuke"
XY = [[1,0],[-1,0],[0,1],[0,-1]]
dist = [[False for _ in range(W)] for _ in range(H)]

dfs(0,0,0)
print("No")