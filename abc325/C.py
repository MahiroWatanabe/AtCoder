# 連結成分　bfs
# 二次元配列を一次元に変換
# unionfindで実装する場合は[x][y]の値を一つの値として判定を行いたい。その場合x*W+yをする
# ことで単一の値に変換することができる
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

H, W = map(int, input().split())
S = [input() for _ in range(H)]
dist = [[-1 for _ in range(W)] for _ in range(H)]
XY = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
index = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "#" and dist[i][j] == -1:
            Que = deque()
            Que.append([i, j])
            dist[i][j] = index
            while Que:
                cx, cy = Que.popleft()
                for dx, dy in XY:
                    x = cx + dx
                    y = cy + dy
                    if (
                        0 <= x < H
                        and 0 <= y < W
                        and S[x][y] == "#"
                        and dist[x][y] == -1
                    ):
                        dist[x][y] = index
                        Que.append([x, y])
            index += 1

S = set()
for i in dist:
    for j in i:
        if j != -1 and j not in S:
            S.add(j)
print(len(S))
