N,K,D = map(int, input().split())
A = list(map(int,input().split()))
dp = [[[-1 for _ in range(100)] for _ in range(105)] for _ in range(105)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(K+1):
        for r in range(D):
            if dp[i][j][r] != -1:
                dp[i+1][j+1][(r+A[i])%D] = max(dp[i+1][j+1][(r+A[i])%D],dp[i][j][r]+A[i])
                dp[i+1][j][r] = max(dp[i+1][j][r],dp[i][j][r])

print(dp[N][K][0])