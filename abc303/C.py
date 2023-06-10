import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,M,H,K = map(int, input().split())
S = input()
XY = [list(map(int, input().split())) for _ in range(M)]
D = defaultdict(int)
for i,j in XY:
    D[(i,j)] = 1
x,y = 0,0

for i in range(N):
    H -= 1
    v = S[i]
    
    if v == "R":
        x += 1
    elif v == "L":
        x -= 1
    elif v == "U":
        y += 1
    else:
        y -= 1
        
    if H < 0:
        print("No")
        exit()
    if H < K and D[(x,y)] == 1:
        D[(x,y)] = 0
        H = K

print("Yes")