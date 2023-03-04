import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
import numpy

N,Q = map(int, input().split())
D = defaultdict(int)

for _ in range(Q):
    c,x = map(int, input().split())
    if c == 1:
        D[x] += 1
    elif c == 2:
        D[x] += 2
    elif c == 3:
        if D[x] >= 2:
            print("Yes")
        else:
            print("No")