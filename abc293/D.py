import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
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
    
N,M = map(int, input().split())
uf = unionfind(N)
x = 0

for _ in range(M):
    A,B,C,D = input().split()
    A,C = int(A)-1,int(C)-1
    
    if uf.same(A,C):
        x += 1
    else:
        uf.merge(A,C)

print(x,N-M)

# import sys, re, string
# from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
# from copy import deepcopy, copy
# from collections import Counter, deque, defaultdict
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
# from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
# from functools import reduce
# from decimal import Decimal, getcontext

# class unionfind:
#     def __init__(self, n):
#         self.n=n
#         self.parent_size=[-1]*n
        
#     def merge(self, a, b):
#         x, y=self.leader(a), self.leader(b)
#         if x == y: return
#         if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
#         self.parent_size[x] += self.parent_size[y]
#         self.parent_size[y]=x
#         return
    
#     def same(self, a, b):
#         return self.leader(a) == self.leader(b)
    
#     def leader(self, a):
#         if self.parent_size[a]<0: return a
#         self.parent_size[a]=self.leader(self.parent_size[a])
#         return self.parent_size[a]
    
#     def size(self, a):
#         return abs(self.parent_size[self.leader(a)])
    
#     def groups(self):
#         result=[[] for _ in range(self.n)]
#         for i in range(self.n):
#             result[self.leader(i)].append(i)
#         return [r for r in result if r != []]
    
# N,M = map(int, input().split())
# uf = unionfind(N)
# x = 0

# for _ in range(M):
#     A,B,C,D = input().split()
#     A,C = int(A)-1,int(C)-1
    
#     if uf.same(A,C):
#         x += 1
#     else:
#         uf.merge(A,C)
        
# T = set()
# for i in range(N):
#     T.add(uf.leader(i))
    
# print(x,len(T)-x)