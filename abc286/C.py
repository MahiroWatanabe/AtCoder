import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

N,A,B = map(int, input().split())
S = input()
ans = 10**18

for i in range(N):
    a,b = S,S[::-1]
    cnt = 0
    
    for j in range(N):
        if a[j] != b[j]:
            cnt += 1
            
    ans = min(ans,i*A+cnt//2*B)
    S = S[1:]+S[0]

print(ans)