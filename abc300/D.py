from math import isqrt

N = int(input())

# sqrt(N) 以下の素数の列挙
sieve = [1] * (isqrt(N) + 1)
primes = []
for p in range(2, len(sieve)):
    if sieve[p] == 0:
        continue
    primes.append(p)
    for j in range(p * p, len(sieve), p):
        sieve[j] = 0

# prefix_sum[n] : (n 以下の素数の個数)
prefix_sum = sieve
for i in range(len(prefix_sum) - 1):
    prefix_sum[i + 1] += prefix_sum[i]

ans = 0

# a, b を全探索する
for i in range(len(primes)):
    a = primes[i]
    if a * a * a * a * a >= N:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a * a * b * b * b >= N:
            break
        ans += prefix_sum[isqrt(N // (a * a * b))] - prefix_sum[b]
print(ans)

# import sys, re, string
# from math import ceil, floor, sqrt, isqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
# from copy import deepcopy, copy
# from collections import Counter, deque, defaultdict
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
# from bisect import bisect, bisect_left, bisect_right
# from functools import reduce
# from decimal import Decimal, getcontext

# def erasto(N):
#     isPrime = [True] * (N+1)
#     isPrime[0] = isPrime[1] = False
#     primes = []

#     for i in range(2,N+1):
#         if isPrime[i]:
#             primes.append(i)
#             for j in range(i*i,N+1,i):
#                 isPrime[j] = False
                
#     return isPrime,primes

# N = int(input())
# isPrime,primes = erasto(10**6)
# ans = 0

# for a in range(len(primes)):
#     if pow(primes[a],5) > N:
#         break
#     for b in range(a+1,len(primes)):
#         if pow(primes[a],2)*pow(primes[b],3) > N:
#             break
#         for c in range(b+1,len(primes)):
#             if pow(primes[a],2)*primes[b]*pow(primes[c],2) > N:
#                 break
#             ans += 1

# print(ans)
