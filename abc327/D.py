# 二部グラフ bipa 01判定 ループ判定
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

sys.setrecursionlimit(10**7)


def bipa(v, status):
    ans[v] = status

    for to in point[v]:
        if ans[to] == 0:
            bipa(to, -status)
        if ans[to] == ans[v]:
            print("No")
            exit()


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
point = [[] for _ in range(N)]
for i in range(M):
    A[i] -= 1
    B[i] -= 1
    point[A[i]].append(B[i])
    point[B[i]].append(A[i])

ans = [0 for _ in range(N)]
for i in range(N):
    if ans[i] == 0:
        bipa(i, 1)

print("Yes")
