import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

N,T = map(int, input().split())
A = [0]+list(map(int,input().split()))
S = sum(A)
A = list(accumulate(A))

for i in range(N+1):
    if T%S <= A[i]:
        print(i,T%S-A[i-1])
        exit()