# 各行、各列にちょうど一個含まれるというのは、1〜Nの順列で表せる
# ABC.で各行の順列を試す方法も解法としてあるが、上に示す方法が簡単
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


def grid_iterator():
    for perm_a in permutations(range(N)):
        for perm_b in permutations(range(N)):
            for perm_c in permutations(range(N)):
                flag = True
                for aj, bj, cj in zip(perm_a, perm_b, perm_c):
                    if len({aj, bj, cj}) != 3:
                        flag = False
                if flag:
                    grid = [["."] * N for _ in range(N)]
                    for i, j in enumerate(perm_a):
                        grid[i][j] = "A"
                    for i, j in enumerate(perm_b):
                        grid[i][j] = "B"
                    for i, j in enumerate(perm_c):
                        grid[i][j] = "C"
                    yield grid


def r_check(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == R[i]:
                break
            return False

    return True


def c_check(grid):
    for j in range(N):
        for i in range(N):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == C[j]:
                break
            return False

    return True


N = int(input())
R = input()
C = input()

for grid in grid_iterator():
    if r_check(grid) and c_check(grid):
        print("Yes")
        for row in grid:
            print(*row, sep="")
        exit()

print("No")
