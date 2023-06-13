import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
A = list(map(int,input().split()))
D = [0]
current_num = 0

for i in range(N-1):
    if i%2 != 0:
        current_num += A[i+1]-A[i]
    D.append(current_num)
    
Q = int(input())

for _ in range(Q):
    l,r = map(int, input().split())
    l_index = bisect_right(A,l)-1
    r_index = bisect_right(A,r)-1
    a = D[r_index]
    if r_index%2 == 1:
        a += r-A[r_index]
    b = D[l_index]
    if l_index%2 == 1:
        b += l-A[l_index]
    print(a-b)