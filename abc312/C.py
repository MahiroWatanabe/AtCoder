import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext

N,M = map(int, input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
left = 1
right = 10**10
print(bisect_right(A,9999))
print(bisect_right(B,9999))

while right-left > 1:
    mid = (left+right)//2
    print(bisect_right(A,mid) ,bisect_right(B,mid))
    if bisect_right(A,mid) >= bisect_right(B,mid):
        left = mid
    else:
        right = mid

print(left)

# import sys, re, string
# from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
# from copy import deepcopy, copy
# from collections import Counter, deque, defaultdict
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
# from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
# from functools import reduce, cmp_to_key
# from decimal import Decimal, getcontext

# def find_min_price(N, M, A, B):
#     C,D = [],[]
#     for i in A:
#         C.append(i)
#         C.append(i+1)
#     for i in B:
#         D.append(i)
#         D.append(i+1)
#     E = sorted(set(C+D))
#     n,m = max(A),max(B)
#     for i in range(len(E)):
        
#         a = bisect_right(A,E[i])
#         b = bisect_right(B,E[i])
#         # if :
#         #     print(E[i])
#         #     exit()
#         if (E[i] > n or E[i] > m) or a >= M-b:
#             print(E[i])
#             exit()

# N, M = map(int, input().split())
# A = sorted(list(map(int, input().split())))
# B = sorted(list(map(int, input().split())))

# result = find_min_price(N, M, A, B)

# print(result)
