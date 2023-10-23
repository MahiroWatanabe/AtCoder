import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

M = int(input())
D = list(map(int,input().split()))
D_A = [0] + list(accumulate(D))
S = (sum(D)+1)//2

for i in range(len(D_A)):
    if S <= D_A[i]:
        print(i,S-D_A[i-1])
        break