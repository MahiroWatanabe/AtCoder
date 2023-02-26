import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def topological_sort(point,num):
    Que = []
    for i in range(len(point)):
        if num[i] == 0:
            heappush(Que,i)
    ans = []
    
    while Que:
        v = heappop(Que)
        ans.append(v+1)
        for nv in point[v]:
            num[nv] -= 1
            if num[nv] == 0:
                heappush(Que,nv)
                
    if len(ans) == N:
        print("Yes")
        print(*ans)
    else:
        print("No")
        
N,M = map(int, input().split())
point = [[] for _ in range(N)]
num = [0]*N
for _ in range(M):
    X,Y = map(int, input().split())
    X,Y = X-1,Y-1
    point[X].append(Y)
    num[Y] += 1

topological_sort(point,num)