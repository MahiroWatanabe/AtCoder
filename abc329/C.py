# ランレングス圧縮の考え
# アルファベット一文字という制限に目をつける
# aaaが存在するのならa,aaも存在する（包含）
# 部分文字列：今回の問題のような前後から一定の区間を削除した（連続している）
# 部分列：文字列から順番通りに連続しない文字列

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
S = input()
abc = [chr(ord("a") + i) for i in range(26)]
E = defaultdict(int)

for i in abc:
    current = ""
    for j in range(N):
        if i != S[j]:
            if current == "":
                continue
            E[i] = max(E[i], len(current))
            current = ""
        else:
            current += i
    if current != "":
        E[i] = max(E[i], len(current))

cnt = 0
for i, j in E.items():
    cnt += j
print(cnt)
