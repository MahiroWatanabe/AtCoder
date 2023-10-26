import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

def dfs(used):
    global ans
    
    if all(used) == True:
        cnt = 0
        for i in range(0,N//2):
            cnt += D[pair[2*i]][pair[2*i+1]]
        ans = max(cnt,ans)
    else:
        x = used.index(False)

        for j in range(x+1,N+1):
            if not used[j]:
                pair.append(x)
                pair.append(j)
                
                used[x] = True
                used[j] = True
                
                dfs(used)
                
                pair.pop()
                pair.pop()
                
                used[x] = False
                used[j] = False

N = int(input())
D = [[0]*(N+1)]

for i in range(1,N):
    d = list(map(int,input().split()))
    d = [0]*(i+1)+d
    D.append(d)

D.append([0]*(N+1))

for i in range(1,N+1):
    for j in range(1,N+1):
        D[j][i] = D[i][j]
used = [False for _ in range(N+1)]
used[0] = True
pair = []
ans = 0

if N%2 == 0:
    dfs(used)
else:
    for i in range(1,N+1):
        used[i] = True
        dfs(used)
        used[i] = False

print(ans)