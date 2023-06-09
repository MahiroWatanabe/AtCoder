import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

W,H = map(int, input().split())
N = int(input())
PQ = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int,input().split()))
B = int(input())
b = list(map(int,input().split()))
D = defaultdict(int)

for i in range(N):
    x = bisect_left(a,PQ[i][0])
    y = bisect_left(b,PQ[i][1])
    D[(x,y)] += 1

m,M = N,0

for i,j in D.items():
    m = min(m,j)
    M = max(M,j)

if len(D) < (A+1)*(B+1):
    m = 0

print(m,M)