# 全探索が無理なら、答えを探索する
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


def is_prime(v):
    v_s = "0" * (N - len(str(v))) + str(v)
    D_C = defaultdict(int)
    for i in v_s:
        D_C[i] += 1
    for i, j in D_C.items():
        if j != D[i]:
            return False

    return True


N = int(input())
S = sorted([int(i) for i in input()])[::-1]
D = defaultdict(int)
tmp = ""
for i in S:
    tmp += str(i)
    D[str(i)] += 1
tmp = int(tmp)
cnt = 0
for i in range(int(sqrt(tmp)) + 1):
    if is_prime(i * i):
        cnt += 1

print(cnt)
