S = input()
N = len(S)
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
MOD = 998244353

for i in range(N):
    for j in range(N):
        if S[i] != ")":
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
        if S[i] != "(" and j > 0:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1] %= MOD
        
print(dp[N][0]%MOD)