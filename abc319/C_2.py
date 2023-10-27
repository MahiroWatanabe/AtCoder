import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def check_condition(p, c):
    def f(i, j, k):
        d = [(p[i], c[i]), (p[j], c[j]), (p[k], c[k])]
        d.sort()
        return d[0][1] != d[1][1]

    if not (f(0, 1, 2) and f(3, 4, 5) and f(6, 7, 8) and
            f(0, 3, 6) and f(1, 4, 7) and f(2, 5, 8) and
            f(0, 4, 8) and f(2, 4, 6)):
        return False

    return True

C = []
for _ in range(3):
    a,b,c = map(int, input().split())
    C.append(a)
    C.append(a)
    C.append(a)
    
cnt = 0
tot = 0

for p in permutations(range(9)):
    if check_condition(p, C):
        cnt += 1
    tot += 1

ans = cnt / tot
print(f"{ans:.10f}")
