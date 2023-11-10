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

# https://atcoder.jp/contests/abc312/tasks/abc312_f
# N, M = map(int, input().split())
# A = []
# B = []
# C = []

# for _ in range(N):
#     T, X = map(int, input().split())
#     if T == 0:
#         A.append(X)
#     elif T == 1:
#         B.append(X)
#     else:
#         C.append(X)
# A = sorted(A)[::-1][:4]
# C = sorted(C[::-1])
# for i in range(len(C)):
