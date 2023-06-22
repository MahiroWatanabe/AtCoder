import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

N,K = map(int, input().split())
A = list(map(int,input().split()))
D = defaultdict(int)

for i in A:
    D[i] += 1

for i in range(K):
    if D[i] == 0:
        print(i)
        exit()

print(K)