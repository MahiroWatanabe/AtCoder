def dfs(i, j):
    cnt = 1
    C[i][j] = "."

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x, y = i + dx, j + dy
            if 0 <= x < H and 0 <= y < W and C[x][y] == "#":
                cnt += dfs(x, y)
    return cnt


H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [0 for _ in range(min(H, W))]

for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            ans[dfs(i, j) // 4 - 1] += 1

print(*ans)
