import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext
XY = [[1,0],[-1,0],[0,1],[0,-1]]

def judge_array(x,y):
    if Q[x][y] or E[x][y] or R[x][y] or T[x][y]:
        return False
    else:
        return True
    
def bfs(start,goal):
    Que = deque()
    Que.append(start)
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[start[0]][start[1]] = 0
            
    while Que:
        x,y = Que.popleft()
        for dx,dy in XY:
            rx = x+dx
            ry = y+dy
            if 0 <= rx < H and 0 <= ry < W:
                if dist[rx][ry] == -1:
                    if A[rx][ry] not in ">v<^#" and judge_array(rx,ry):
                        dist[rx][ry] = dist[x][y] + 1
                        Que.append([rx,ry])
    
    print(dist[goal[0]][goal[1]])

H,W = map(int, input().split())
A = [list(input()) for _ in range(H)]
Q = [[False for _ in range(W)] for _ in range(H)]
E = [[False for _ in range(W)] for _ in range(H)]
R = [[False for _ in range(W)] for _ in range(H)]
T = [[False for _ in range(W)] for _ in range(H)]
start,goal = [0,0],[0,0]

for i in range(H):
    flag = False
    for j in range(W):
        if A[i][j] == "S":
            start = [i,j]
        if A[i][j] == "G":
            goal = [i,j]
        if A[i][j] == ">":
            flag = True
        elif flag and A[i][j] in ">v<^#":
            flag = False
        elif flag and A[i][j] == ".":
            Q[i][j] = True
            
for i in range(H-1,-1,-1):
    flag = False
    for j in range(W-1,-1,-1):
        if A[i][j] == "<":
            flag = True
        elif flag and A[i][j] in ">v<^#":
            flag = False
        elif flag and A[i][j] == ".":
            E[i][j] = True
            
for i in range(W):
    flag = False
    for j in range(H):
        if A[j][i] == "v":
            flag = True
        elif flag and A[j][i] in ">v<^#":
            flag = False
        elif flag and A[j][i] == ".":
            R[j][i] = True
            
for i in range(W-1,-1,-1):
    flag = False
    for j in range(H-1,-1,-1):
        if A[j][i] == "^":
            flag = True
        elif flag and A[j][i] in ">v<^#":
            flag = False
        elif flag and A[j][i] == ".":
            T[j][i] = True   

bfs(start,goal)