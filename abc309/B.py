N = int(input())
A = [input() for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1,N):
    ans[0][i] = A[0][i-1]

for i in range(1,N):
    ans[i][N-1] = A[i-1][N-1]

for i in range(N-2,-1,-1):
    ans[N-1][i] = A[N-1][i+1]

for i in range(N-2,-1,-1):
    ans[i][0] = A[i+1][0]

for i in range(N):
    for j in range(N):
        if i == 0 or j == 0 or i == N-1 or j == N-1:
            print(ans[i][j],sep="",end="")
        else:
            print(A[i][j],sep="",end="")
    print()