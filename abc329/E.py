# 逆から見ていく
from collections import deque


def main():
    n, m = map(int, input().split())
    s, t = list(input()), list(input())

    used = [False] * n
    q = deque()

    def push(i):
        nonlocal used
        if i < 0 or i + m > n:
            return
        if used[i]:
            return
        for j in range(m):
            if s[i + j] != "?" and s[i + j] != t[j]:
                return
        used[i] = True
        q.append(i)

    for i in range(n - m + 1):
        push(i)

    while q:
        i = q.popleft()
        for j in range(m):
            s[i + j] = "?"
        for ni in range(i - m + 1, i + m):
            push(ni)

    for i in s:
        if i != "?":
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
