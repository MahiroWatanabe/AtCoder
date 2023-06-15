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
D = []
S = set()
heapify(D)
for i in A:
    if i not in S:
        heappush(D,i)
        S.add(i)

for i in range(K-1):
    v = heappop(D)
    for j in range(N):
        num = v+A[j]
        if num not in S:
            heappush(D,num)
            S.add(num)

print(min(D))