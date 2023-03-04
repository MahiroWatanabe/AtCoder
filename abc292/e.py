import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
import numpy

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
                
    return ans

N,M = map(int, input().split())
point = [[] for _ in range(N)]
num = [0]*N

if M == 0:
    print(0)
    exit()
    
for _ in range(M):
    u,v = map(int, input().split())
    u,v = u-1,v-1
    point[u].append(v)
    num[v] += 1

topo = topological_sort(point,num)
cnt = 0
print(topo)
for i in range(len(topo)):
    print()