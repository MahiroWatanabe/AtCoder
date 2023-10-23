import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce, cmp_to_key
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

def find_reading_order(N, prerequisites):
    # 先行条件を満たす本を格納するリスト
    reading_order = []
    
    # 本ごとの先行条件の情報を辞書にまとめる
    prerequisites_dict = {}
    for i in range(N):
        Ci, *Pi = prerequisites[i]
        prerequisites_dict[i+1] = Pi
    
    # 先行条件を満たす本を探索する関数
    def dfs(book):
        nonlocal reading_order
        if book not in reading_order:
            for prereq in prerequisites_dict[book]:
                dfs(prereq)
            reading_order.append(book)
    
    # 本1を読むために必要な本を探索
    dfs(1)
    
    # 本1以外の読むべき本を出力
    return ' '.join(map(str, [book for book in reading_order if book != 1]))

# 入力を受け取る
N = int(input())
prerequisites = [list(map(int, input().split())) for _ in range(N)]

# 関数を呼び出し、結果を出力
result = find_reading_order(N, prerequisites)
print(result)
