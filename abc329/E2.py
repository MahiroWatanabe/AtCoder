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


def f(v):
    if 0 <= v <= N - M and not used[v]:
        flag = True
        for j in range(M):
            if v + j < N:
                if not (S[v + j] == T[j] or S[v + j] == "#"):
                    flag = False
        if flag:
            used[v] = True
            D.append(v)


N, M = map(int, input().split())
S = list(input())
T = list(input())
D = deque()
used = [False for _ in range(N)]

for i in range(N):
    f(i)

while D:
    v = D.popleft()

    for i in range(M):
        S[v + i] = "#"

    for i in range(v - M + 1, v + M):
        f(i)

for i in S:
    if i != "#":
        print("No")
        exit()
print("Yes")
