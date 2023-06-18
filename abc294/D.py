import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

class MultiSet():
    def __init__(self):
        self.heap = []
        self.dict = {}
    
    def add(self, x):
        heappush(self.heap, x)
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1
    
    def delete(self, x):
        if x not in self.dict or self.dict[x] == 0: sys.exit()
        else: self.dict[x] -= 1
 
        while len(self.heap) > 0:
            val = heappop(self.heap)
            if self.dict[val] > 0:
                heappush(self.heap, val)
                break
    
    def exists(self, x):
        return x in self.dict and self.dict[x] > 0
 
    def get_min(self):
        return self.heap[0]
 
    def is_empty(self):
        return len(self.heap) == 0
    
N,Q = map(int, input().split())
muti = MultiSet()
index = 1

for _ in range(Q):
    v,*_a = map(int, input().split())
    if v == 1:
        muti.add(index)
        index += 1
    elif v == 2:
        x = _a[0]
        muti.delete(x)
    else:
        print(muti.get_min())