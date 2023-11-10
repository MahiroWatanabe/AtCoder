import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import (
    accumulate,
    product,
    combinations,
    combinations_with_replacement,
    permutations,
    groupby,
)
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

N = int(input())
P = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        D = copy(P)
        a, b = P[i], P[j]
        D[i] = b
        D[j] = a
        flag = True
        # print(D)
        for k in range(1, N):
            if not D[k - 1] < D[k]:
                flag = False
        if flag:
            print("YES")
            exit()
print("NO")
