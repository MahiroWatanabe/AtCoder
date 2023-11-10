# 部分木問題　根（最頂点）から木構造を見ていき配列にそれぞれの頂点のデータを保持しておく
# 今回の問題はK[i]番目（最大値20）の要素まで見れればいいので、頂点からのデータを保持して考える
# 再帰が終わるタイミングで配列に格納することで、包含関係にある頂点のデータを管理できる

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


def dfs(v):
    ans[v].append(X[v])
    dist[v] = True
    for to in point[v]:
        if not dist[to]:
            dfs(to)
            ans[v].extend(ans[to])
    ans[v].sort(reverse=True)
    ans[v] = ans[v][:20]


N, Q = map(int, input().split())
X = list(map(int, input().split()))
point = [[] for _ in range(N)]
ans = [[] for _ in range(N)]

for _ in range(N - 1):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    point[A].append(B)
    point[B].append(A)
dist = [False for _ in range(N)]

dfs(0)

for _ in range(Q):
    V, K = map(int, input().split())
    V -= 1
    print(ans[V][K - 1])
