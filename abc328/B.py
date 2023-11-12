# 文字列をset()に入れると分割されて考えられる
# 例：set("ABC") = {"A","B","C"}
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
D = list(map(int, input().split()))
cnt = 0

for i in range(N):
    current = str(i + 1)
    v = str(D[i])
    S = set()
    for j in range(len(current)):
        S.add(current[j])
    for j in range(1, D[i] + 1):
        E = copy(S)
        pre = str(j)
        for k in range(len(pre)):
            E.add(pre[k])
        if len(E) == 1:
            cnt += 1

print(cnt)
