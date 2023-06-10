import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,M = map(int, input().split())
S = [input() for _ in range(N)]

for D in permutations(S,N):
    flag = True
    for i in range(N-1):
        cnt = 0
        for j in range(M):
            if D[i][j] != D[i+1][j]:
                cnt += 1
        if cnt > 1:
            flag = False
    if flag:
        print("Yes")
        exit()

print("No")