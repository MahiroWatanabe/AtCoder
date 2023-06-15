import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

N,M = map(int, input().split())

ans = 20**20
for i in range(1,int(sqrt(M))+2):
    v = ceil(M/i)
    x = M//i
    
    if i <= N and v <= N and M <= i*v:
        ans = min(ans,i*v)
    
    if i <= N and x <= N and M <= i*x:
        ans = min(ans,i*x)
    
print(ans if ans != 20**20 else -1)