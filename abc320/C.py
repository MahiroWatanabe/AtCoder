import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

M = int(input())
S1,S2,S3 = [],[],[]
d = input()
for j in d:
    S1.append(int(j))
d = input()
for j in d:
    S2.append(int(j))
d = input()
for j in d:
    S3.append(int(j))
S1 = S1*3
S2 = S2*3
S3 = S3*3
D = [S1,S2,S3]
ans = 10**10

for data in permutations(D):
    F = [False for _ in range(M*3+1)]
    
    for i in range(10):
        a,b,c = 10**10,10**10,10**10
        
        if i in data[0]:
            a = data[0].index(i)
            if i in data[1][a+1:]:
                b = data[1][a+1:].index(i)+a+1
                if i in data[2][b+1:]:
                    c = data[2][b+1:].index(i)+b+1
                    ans = min(ans,max(a,b,c))

print(ans if ans != 10**10 else -1)

# もっと簡単な実装
# M = int(input())
# N = 3
# S = [input() for _ in range(N)]
# INF = 1e9
# ans = INF
# for i in range(N * M):
#     for j in range(N * M):
#         for k in range(N * M):
#             if i != j and i != k and j != k and S[0][i % M] == S[1][j % M] == S[2][k % M]:
#                 ans = min(ans, max(i, j, k))
# print(ans if ans < INF else -1)
