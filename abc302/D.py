import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,M,D = map(int, input().split())
A = sorted(list(map(int,input().split())))
B = list(map(int,input().split()))
ans = -1

for i in range(M):
    index = bisect_right(A,B[i]+D)-1
    if 0 <= index and A[index] >= B[i]-D:
        ans = max(ans,A[index]+B[i])

print(ans)