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

N, M = map(int, input().split())
S = list(input())
ans = copy(S)
T = list(input())
# ans = ["x" for _ in range(N)]

for data in permutations(T):
    # print(data)
    for i in range(M - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if S[j] == data[i]:
                # print(i, j)
                for k in range(M):
                    if j - k >= 0 and i - k >= 0:
                        if S[j - k] != data[i]:
                            S[j - k] = data[i - k]
    # print(S)
    current = 0
    for i in range(N):
        flag = True
        if ans[i] == T[0]:
            for j in range(M):
                if i + j < N:
                    if ans[i + j] != T[j]:
                        flag = False
                else:
                    flag = False
            if flag:
                # print("AAA")
                for j in range(M):
                    S[i + j] = T[j]

    # print(S)
    flag = True
    for i in range(N):
        if S[i] != ans[i]:
            flag = False
    if flag:
        print("Yes")
        exit()
print("No")
