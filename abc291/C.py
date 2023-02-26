import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
S = input()
A = defaultdict(bool)
A[0,0] = True
x,y = 0,0

for i in range(len(S)):
    if S[i] == "R":
        x,y = x+1,y
    elif S[i] == "L":
        x,y = x-1,y
    elif S[i] == "U":
        x,y = x,y+1
    elif S[i] == "D":
        x,y = x,y-1
    if A[x,y] == True:
        print("Yes")
        exit()
    A[x,y] = True
print("No")