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

N = int(input())
cnt = 0

for a in range(1,N+1):
    for b in range(1,(N-a)+1):
        if a*b >= N:
            break
        for c in range(1,N+1):
            d = (N-a*b)//c
            if 1 <= d <= N and a*b+c*d == N:
                cnt += 1

print(cnt)