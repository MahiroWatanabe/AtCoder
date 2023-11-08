# トポロジカルソート　大きい値から小さい値に辺を引く
# DAG（サイクルの無い有効グラフ）
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


def topological_sort(point, num):
    Que = deque()
    for i in range(len(point)):
        if num[i] == 0:
            Que.append(i)
    ans = [0] * N
    na = N
    while Que:
        if len(Que) >= 2:
            print("No")
            exit()
        v = Que.popleft()
        ans[v] = na
        na -= 1
        for nv in point[v]:
            num[nv] -= 1
            if num[nv] == 0:
                Que.append(nv)

    if len(ans) == N:
        print("Yes")
        print(*ans)
    else:
        print("No")


N, M = map(int, input().split())
point = [[] for _ in range(N)]
num = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    point[B].append(A)
    num[A] += 1

topological_sort(point, num)
