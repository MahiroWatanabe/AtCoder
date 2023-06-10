H,W = map(int, input().split())
S = [input() for _ in range(H)]
XY = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
judge = "snuke"
S_A = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            S_A.append([i,j])

for i in range(len(S_A)):
    for direction in range(8):
        ans = []
        ans.append([S_A[i][0]+1,S_A[i][1]+1])
        dx,dy = XY[direction]
        x,y = S_A[i][0],S_A[i][1]
        flag = True
        for j in range(1,5):
            x,y = x+dx,y+dy
            if 0 <= x < H and 0 <= y < W:
                if S[x][y] == judge[j]:
                    ans.append([x+1,y+1])
                else:
                    flag = False
                    break
            else:
                flag = False
        if flag:
            for point in ans:
                print(*point)
            exit()