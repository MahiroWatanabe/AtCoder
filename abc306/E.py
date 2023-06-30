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
A = list(map(int,input().split()))
D = [0]
num = 0
for i in range(N-1):
    if i%2 == 1:
        num += A[i+1]-A[i]
    D.append(num)
    
Q = int(input())
for _ in range(Q):
    l,r = map(int, input().split())
    L = bisect_right(A,l)-1
    R = bisect_right(A,r)-1
    a,b = D[L],D[R]
    if L%2 == 1:
        a += l-A[L]
    if R%2 == 1:
        b += r-A[R]
    print(b-a)