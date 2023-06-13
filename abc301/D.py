import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def f(s):
    D = copy(s)
    for i in range(len(D)):
        if D[i] == "?":
            D[i] = "0"
    value = int("".join(D),2)
    if value <= N:
        return True
    else:
        return False

S = list(input())
N = int(input())
D = copy(S)
if not f(D):
    print(-1)
    exit()

for i in range(len(S)):
    if S[i] == "?":
        S[i] = "1"
        if not f(S):
            S[i] = "0"
            
print(int("".join(S),2))