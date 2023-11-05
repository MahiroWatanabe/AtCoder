# Dijkstra　ダイクストラ法　二つのグラフを使用して考える
# 頂点1から特定の頂点の最短距離を求める（Aとする）、頂点Nから特定の頂点の最短距離を求める（Bとする）
# その場合A[特定の頂点]+B[特定の頂点]で最短距離を求めることができる
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


def Dijkstra(pos, b, c):
    INF = 20**20
    ans = [False] * N
    cur = [INF] * N
    cur[pos] = 0
    Que = []
    heappush(Que, [cur[pos], pos])
    while Que:
        v = heappop(Que)[1]
        if ans[v] == True:
            continue
        ans[v] = True
        for to in point[v]:
            if cur[to[0]] > cur[v] + to[1] * b + c:
                cur[to[0]] = cur[v] + to[1] * b + c
                heappush(Que, [cur[to[0]], to[0]])
    return cur


N, A, B, C = map(int, input().split())
point = [[] for _ in range(N)]
for i in range(N):
    D = list(map(int, input().split()))
    for j in range(N):
        point[i].append([j, D[j]])

Q = Dijkstra(0, A, 0)
W = Dijkstra(N - 1, B, C)
ans = 20**20

for i in range(N):
    ans = min(ans, Q[i] + W[i])
print(ans)
