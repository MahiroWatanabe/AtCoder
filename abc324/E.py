# 部分列判定
# Pythonは文字列の計算量が多いので、共通化できる部分は基本的にfor文の外に出して考える
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

N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]
L, R = [], []
RT = T[::-1]

for i in range(N):
    current = S[i]
    tmp = 0
    index = 0
    while tmp < len(T) and index < len(current):
        if current[index] == T[tmp]:
            index += 1
            tmp += 1
        else:
            index += 1
    L.append(tmp)

    current = S[i][::-1]
    tmp = 0
    index = 0
    while tmp < len(T) and index < len(current):
        if current[index] == RT[tmp]:
            index += 1
            tmp += 1
        else:
            index += 1
    R.append(tmp)
R.sort()

cnt = 0
for i in range(N):
    v = bisect_left(R, len(T) - L[i])
    cnt += N - v
print(cnt)
