# 全域木　MST
# 頂点数と辺の数から計算量の見積もりを行う。
# 全域木は N-1の辺があれば成立するので、与えられた辺からmCn-1取り出す
# 木の判定はunionfindを用いて行うことで、高速に実装できる
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


class unionfind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


N, M, K = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]
ans = 20**20
for data in combinations([i for i in range(M)], N - 1):
    uf = unionfind(N)
    current = 0
    flag = False
    for i in range(N - 1):
        u, v = UV[data[i]][0] - 1, UV[data[i]][1] - 1
        if uf.same(u, v):
            flag = True
            break
        uf.merge(u, v)
        current += UV[data[i]][2]
    if not flag:
        ans = min(ans, current % K)

print(ans)
