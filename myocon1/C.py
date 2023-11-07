# GCDは順序によらず一定である
# 間の数だけを抜いて考えたい時は左右からの累積和を使用する
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
A = list(map(int, input().split()))

if N == 2:
    print(max(A))
    exit()

L = [A[0]]
for i in range(1, N - 1):
    L.append(gcd(L[-1], A[i]))

B = A[::-1]
R = [B[0]]
for i in range(1, N - 1):
    R.append(gcd(R[-1], B[i]))

ans = max(L[-1], R[-1])
for i in range(1, N - 1):
    ans = max(ans, gcd(L[i - 1], R[N - i - 2]))

print(ans)
