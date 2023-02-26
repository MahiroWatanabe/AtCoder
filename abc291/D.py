MOD = 998244353

N = int(input())
A = []
B = []
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0, 0] for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    x = i-1
    while x > 0 and B[x-1] != A[i-1]:
        x -= 1
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
    dp[i][1] = (dp[i-1][0] - dp[x][0] + dp[i-1][1] - dp[x][1]) % MOD

print((dp[N][0] + dp[N][1]) % MOD)
