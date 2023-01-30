import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
cnt1 = 0
cnt2 = 0
for _ in range(N):
    S = input()
    if S == "For":
        cnt1 += 1
    else:
        cnt2 += 1

print("Yes" if cnt1 >= ceil(N/2) else "No")