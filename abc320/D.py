# bfs　グラフに変換する問題　
# 特殊な部分はダイクストラ法のように辺に重り（dx,dy）があること
# （dx,dy）をdefaultdictで持つことで、O(1)で参照できる

import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def bfs(S):
    Que = deque()
    Que.append(S)
    ans = [[0,0] for _ in range(N)]
    judge = [False for _ in range(N)]
    judge[0] = True
    
    while Que:
        v = Que.popleft()
        for to in point[v]:
            if not judge[to]:
                ans[to] = [ans[v][0]+D[(v,to)][0],ans[v][1]+D[(v,to)][1]]
                judge[to] = True
                Que.append(to)
    
    for i in range(N):
        if not judge[i]:
            print("undecidable")
        else:
            print(*ans[i])

N,M = map(int, input().split())
point = [[] for _ in range(N)]
D = defaultdict(list)
for _ in range(M):
    A,B,X,Y = map(int, input().split())
    A -= 1
    B -= 1
    point[A].append(B)
    point[B].append(A)
    if len(D[(A,B)]) == 0:
        D[(A,B)] = [X,Y]
        D[(B,A)] = [-X,-Y]

bfs(0)