import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

S = input()
T = deque()
flag = False
for i in range(len(S)):
    if S[i] == "R":
        flag = not flag
    else:
        if flag:
            T.appendleft(S[i])
            if len(T) >= 2:
                a = T.popleft()
                b = T.popleft()
                if a != b:
                    T.appendleft(b)
                    T.appendleft(a)
        else:
            T.append(S[i])
            if len(T) >= 2:
                a = T.pop()
                b = T.pop()
                if a != b:
                    T.append(b)
                    T.append(a)

if flag:
    T = reversed(T)

print("".join(T))