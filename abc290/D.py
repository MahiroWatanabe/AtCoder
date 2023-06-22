import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

T = int(input())

for _ in range(T):
    N,D,K = map(int, input().split())
    K -= 1
    g = gcd(N,D)
    m = N//g
    e = D//g
    b = K*e%m
    i = K//m
    ans = b*g+i
    print(ans)