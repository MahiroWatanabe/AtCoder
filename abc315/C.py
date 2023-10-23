N = int(input())
FS = [list(map(int, input().split())) for _ in range(N)]
a,b = 0,0
index = 0
for i in range(N):
    if b < FS[i][1]:
        a,b = FS[i][0],FS[i][1]
        index = i

ans = 0
for i in range(N):
    if index != i:
        if a != FS[i][0]:
            ans = max(ans,b+FS[i][1])
        else:
            ans = max(ans,b+FS[i][1]//2)

print(ans)