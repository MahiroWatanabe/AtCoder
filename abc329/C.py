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
S = input()
abc = [chr(ord("a") + i) for i in range(26)]
D = set()
E = defaultdict(int)

for i in abc:
    # print(i)
    current = ""
    for j in range(N):
        if i != S[j]:
            # print("AAA")
            if current == "":
                continue
            # D.add(current)
            # print(current)
            E[i] = max(E[i], len(current))
            current = ""
        else:
            current += i
    if current != "":
        E[i] = max(E[i], len(current))

# print(D)
# print(len(D)
# print(E)
cnt = 0
for i, j in E.items():
    cnt += j
print(cnt)
