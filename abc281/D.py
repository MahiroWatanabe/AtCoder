N,K,D = map(int, input().split())
A = list(map(int,input().split()))
dp = [[[-1 for _ in range(100)] for _ in range(105)] for _ in range(105)]
dp[0][0][0] = 0

for i in range(N):
    ni = i+1
    for j in range(K+1):
        for r in range(D):
            if dp[i][j][r] != -1:
                nj = j+1
                nr = (r+A[i])%D
                dp[ni][nj][nr] = max(dp[ni][nj][nr],dp[i][j][r]+A[i])
                
                nj = j
                nr = r
                dp[ni][nj][nr] = max(dp[ni][nj][nr],dp[i][j][r])

print(dp[N][K][0])