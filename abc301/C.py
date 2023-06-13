import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

S = input()
T = input()
D = defaultdict(int)
F = defaultdict(int)
judge = "atcoder"
for i in S:
    D[i] += 1

for i in T:
    F[i] += 1

R = []
r = 0
for i,j in D.items():
    if i == "@":
        continue
    if F[i] == 0:
        R.append(i)
        r += j
    else:
        if F[i] < j:
            R.append(i)
            r += j-F[i]
for i in R:
    if i not in judge:
        print("No")
        exit()
if F["@"] < r:
    print("No")
    exit()

R = []
r = 0
for i,j in F.items():
    if i == "@":
        continue
    if D[i] == 0:
        R.append(i)
        r += j
    else:
        if D[i] < j:
            R.append(i)
            r += j-D[i]
for i in R:
    if i not in judge:
        print("No")
        exit()
if D["@"] < r:
    print("No")
    exit()

print("Yes")