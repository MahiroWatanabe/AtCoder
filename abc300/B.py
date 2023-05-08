def judge(s, t):
    for i in range(H):
        for j in range(W):
            if A[(i - s) % H][(j - t) % W] != B[i][j]:
                return False

    return True


H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if judge(i, j):
            print("Yes")
            exit()

print("No")
