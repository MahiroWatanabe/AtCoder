import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
D = defaultdict(int)
c = []
i, j = 0, 0
cnt = 0
while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        D[a[i]] = cnt
        i += 1
    else:
        c.append(b[j])
        D[b[j]] = cnt
        j += 1
    cnt += 1

# AとBの残りの要素を追加する
while i < n:
    c.append(a[i])
    D[a[i]] = cnt
    i += 1
    cnt += 1
while j < m:
    c.append(b[j])
    D[b[j]] = cnt
    j += 1
    cnt += 1


ans = []

for i in a:
    ans.append(D[i]+1)
print(*ans)

ans2 = []

for i in b:
    ans2.append(D[i]+1)
print(*ans2)