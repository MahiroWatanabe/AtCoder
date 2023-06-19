def dfs(x,y,D):
    global ans
    if A[x][y] in D:
        return
    if x == H-1 and y == W-1:
        ans += 1
        
    D.add(A[x][y])
    for dx,dy in XY:
        cx,cy = x+dx,y+dy
        if 0 <= cx < H and 0 <= cy < W:
            dfs(cx,cy,D)
    D.discard(A[x][y])

H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
XY = [[1,0],[0,1]]
ans = 0

dfs(0,0,set())

print(ans)