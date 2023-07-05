import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def mex(x,y,z):
    for i in range(3):
        if x != i and y != i and z != i:
            return i
    return 3

N = int(input())
A = list(map(int,input().split()))
S = input()

cnt_l = [[0 for _ in range(3)] for _ in range(N+1)]
cnt_r = [[0 for _ in range(3)] for _ in range(N+1)]

for i in range(N):
    cnt_l[i+1] = copy(cnt_l[i])
    if S[i] == "M":
        cnt_l[i+1][A[i]] += 1
        
for i in range(N-1,-1,-1):
    cnt_r[i] = copy(cnt_r[i+1])
    if S[i] == "X":
        cnt_r[i][A[i]] += 1

print(*cnt_l)
print(*cnt_r)
ans = 0
for i in range(N):
    if S[i] == "E":
        for j in range(3):
            for k in range(3):
                # 前から見たときは0が加えられてるのでi
                # 例:0MEEX
                # 後ろから見たときは0がないのでi+1する
                # 例:MEEX0
                # 添え字が合わないのでずらす必要がある
                ans += cnt_l[i][j]*cnt_r[i+1][k]*mex(j,A[i],k)

print(ans)