# 3×3問題
import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import (
    accumulate,
    product,
    combinations,
    combinations_with_replacement,
    permutations,
    groupby,
)
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def f(row, col, q, p):
    for i in range(3):
        if C[row[i][0][0]][row[i][0][1]] == C[row[i][1][0]][row[i][1][1]] and C[row[i][0][0]][row[i][0][1]] != C[row[i][2][0]][row[i][2][1]]:
            return False
    
    for i in range(3):
        if C[col[i][0][0]][col[i][0][1]] == C[col[i][1][0]][col[i][1][1]] and C[col[i][0][0]][col[i][0][1]] != C[col[i][2][0]][col[i][2][1]]:
            return False
    
    if C[q[0][0]][q[0][1]] == C[q[1][0]][q[1][1]] and C[q[0][0]][q[0][1]] != C[q[2][0]][q[2][1]]:
            return False
        
    if C[p[0][0]][p[0][1]] == C[p[1][0]][p[1][1]] and C[p[0][0]][p[0][1]] != C[p[2][0]][p[2][1]]:
            return False
        
    return True

C = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
tmp = 0
D = []
for i in range(3):
    for j in range(3):
        D.append([i, j])

for data in permutations(D):
    row = [[] for _ in range(3)]
    col = [[] for _ in range(3)]
    q = []
    p = []

    for i in range(9):
        row[data[i][0]].append([data[i][0], data[i][1]])
        col[data[i][1]].append([data[i][0], data[i][1]])
        if data[i][0] == data[i][1]:
            q.append([data[i][0], data[i][1]])
        if abs(data[i][0] - data[i][1]) >= 2 or (data[i][0] == 1 and data[i][1] == 1):
            p.append([data[i][0], data[i][1]])

    if f(row, col, q, p):
        cnt += 1

    tmp += 1

print(cnt / tmp)
