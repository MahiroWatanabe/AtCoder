import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

T = int(input())
for _ in range(T):
    N = int(input())
    
    for i in range(2,N+1):
        if pow(i,3) > N:
            break
        if N % i == 0:
            break
    if N%i**2 == 0:
        print(i,N//i**2)
    else:
        print(int(sqrt(N//i)), i)