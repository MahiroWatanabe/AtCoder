H,W = map(int, input().split())
S = [input() for _ in range(H)]
XY = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(H):
    for j in range(W):
        cnt = 0
        if S[i][j] == ".":
            for dx,dy in XY:
                if 0 <= i+dx < H and 0 <= j+dy < W:
                    if S[i+dx][j+dy] == "#":
                        cnt += 1
            if cnt >= 2:
                print(i+1,j+1)
                exit()