import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
AB = [list(map(Decimal, input().split())) for _ in range(N)]
D = []

for i in range(N):
    num = AB[i][0]/(AB[i][0]+AB[i][1])
    D.append([num,i+1])
# 一番目を降順、二番目を昇順に並べる方法
D = sorted(D,key=lambda x:(-x[0], x[1]))

for i,j in D:
    print(j)