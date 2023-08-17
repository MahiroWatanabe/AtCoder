# 事前に二部グラフの判定を行っておきく
# その中で、辺を追加した後に、今回の条件を満たすのは、
# 違う連結成分を連結したときと同じ連結成分の違う色の点を連結したときになる
# そして、その数を求めるには、それぞれの色の数「２：４」などを持って置き、
# 連結成分も色も同じでない場合の組み合わせを求める。
# 今回は上記の条件を反転させた方が楽に解法を求められる。

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

def c2(n):
    return n*(n-1)//2

def dfs(v,color):
    colors[v] = color
    cvs[color] += 1
    for to in point[v]:
        if colors[to] == color:
            return False
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True

def is_bipartite(index):
    return dfs(index,1)

N,M = map(int, input().split())
point = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int, input().split())
    A -= 1
    B -= 1
    point[A].append(B)
    point[B].append(A)

ans = c2(N)-M 
colors = [0 for _ in range(N)]

for i in range(N):
    if colors[i] != 0:
        continue
    
    cvs = defaultdict(int)
    
    if not is_bipartite(i):
        print(0)
        exit()
        
    for j,k in cvs.items():
        ans -= c2(k)

print(ans)