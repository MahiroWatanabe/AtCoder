N = int(input())
ans = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    A,B,C,D = map(int, input().split())
    for i in range(A,B):
        for j in range(C,D):
            if ans[i][j] == 0:
                ans[i][j] = 1
cnt = 0
for i in ans:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)