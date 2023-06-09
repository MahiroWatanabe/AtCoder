import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

class unionfind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n
        
    def merge(self, a, b):
        x, y=self.leader(a), self.leader(b)
        if x == y: return
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return
    
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    
    def leader(self, a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    
    def size(self, a):
        return abs(self.parent_size[self.leader(a)])
    
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

N,D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
uf = unionfind(N)

for i in range(N):
    for j in range(N):
        if i != j:
            diff = sqrt((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)
            if diff <= D:
                if not uf.same(i,j):
                    uf.merge(i,j)

for i in range(N):
    if uf.same(0,i):
        print("Yes")
    else:
        print("No")