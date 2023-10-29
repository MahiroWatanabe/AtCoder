import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

N,M,P = map(int, input().split())
A = list(map(int,input().split()))
B = sorted(list(map(int,input().split())))
C = [0] + list(accumulate(B))
ans = 0

for i in range(N):
    v = P-A[i]
    v_index = bisect_right(B,v)
    v1_index = bisect_left(B,v)
    ans += (M-v_index)*P
    ans += C[v_index]+v_index*A[i]
print(ans)