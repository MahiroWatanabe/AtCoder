import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def factorization(n,D):
    arr = []
    temp = n
    for i in D:
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
        
    return arr

T = int(input())
MOD = 10**6
for _ in range(T):
    N = int(input())
    isPrime = [True] * (MOD+1)
    isPrime[0] = isPrime[1] = False

    for i in range(2,MOD+1):
        if isPrime[i]:
            for j in range(i*i,MOD+1,i):
                isPrime[j] = False
    D = []
    for i in range(len(isPrime)):
        if isPrime[i] == True:
            D.append(i)
    A = factorization(N,D)
    A = sorted(A,key= lambda x:x[1],reverse=True)
    print(A[0][0],A[1][0])
        