H, W = map(int, input().split())
XY = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
S = [input() for _ in range(H)]
ans = [["#" for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            cnt = 0
            for dx, dy in XY:
                x = i + dx
                y = j + dy
                if 0 <= x < H and 0 <= y < W and S[x][y] == "#":
                    cnt += 1
            ans[i][j] = str(cnt)

for i in ans:
    print(*i, sep="")
