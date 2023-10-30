# 文字列回転　実装が難しい
# オフセット使った考え

import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

def change_array(req,cnt):
    for _ in range(cnt):
        req = [list(a)[::-1] for a in zip(*req)]
    return req

def find_array(req):
    for i in range(4):
        for j in range(4):
            if req[i][j] == "#":
                return i,j

A,B,C = [],[],[]
cnt_a,cnt_b,cnt_c = 0,0,0
for _ in range(4):
    P = input()
    D = []
    for i in P:
        if i == "#":
            cnt_a += 1
        D.append(i)
    A.append(D)
for _ in range(4):
    P = input()
    D = []
    for i in P:
        if i == "#":
            cnt_b += 1
        D.append(i)
    B.append(D)
for _ in range(4):
    P = input()
    D = []
    for i in P:
        if i == "#":
            cnt_c += 1
        D.append(i)
    C.append(D)

for I in range(4):
    for J in range(4):
        for K in range(4):
            Q,W,E = change_array(A,I),change_array(B,J),change_array(C,K)
            Qx,Qy = find_array(Q)
            Wx,Wy = find_array(W)
            Ex,Ey = find_array(E)
            for qi in range(4):
                for qj in range(4):
                    for wi in range(4):
                        for wj in range(4):
                            for ei in range(4):
                                for ej in range(4):
                                    check = [["." for _ in range(4)] for _ in range(4)]
                                    flag = False
                                    flag2 = False
                                    offset_qi = Qx-qi
                                    offset_qj = Qy-qj
                                    offset_wi = Wx-wi
                                    offset_wj = Wy-wj
                                    offset_ei = Ex-ei
                                    offset_ej = Ey-ej
                                    cnt_q,cnt_w,cnt_e = 0,0,0
                                    
                                    for i in range(4):
                                        for j in range(4):
                                            ii = i+offset_qi
                                            jj = j+offset_qj
                                            if 0 <= ii < 4 and 0 <= jj < 4:
                                                if Q[ii][jj] == "#":
                                                    check[i][j] = "#"
                                                    cnt_q += 1
                                    if cnt_q != cnt_a:
                                        continue
                                    
                                    for i in range(4):
                                        for j in range(4):
                                            ii = i+offset_wi
                                            jj = j+offset_wj
                                            if 0 <= ii < 4 and 0 <= jj < 4:
                                                if W[ii][jj] == "#":
                                                    if check[i][j] == "#":
                                                        flag = True
                                                    check[i][j] = "#"
                                                    cnt_w += 1
                                    if cnt_w != cnt_b:
                                        continue
                                    
                                    for i in range(4):
                                        for j in range(4):
                                            ii = i+offset_ei
                                            jj = j+offset_ej
                                            if 0 <= ii < 4 and 0 <= jj < 4:
                                                if E[ii][jj] == "#":
                                                    if check[i][j] == "#":
                                                        flag = True
                                                    check[i][j] = "#"
                                                    cnt_e += 1
                                    if cnt_e != cnt_c:
                                        continue
                                    
                                    for i in range(4):
                                        for j in range(4):
                                            if check[i][j] != "#":
                                                flag2 = True
                                                
                                    if not flag and not flag2:
                                        print("Yes")
                                        exit()
                                        
print("No")                 