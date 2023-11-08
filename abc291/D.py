# dp問題
# MOD問題は値が更新される度にMODを行う。そうしないとTLE or MLEになる
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
dp[0][0] = dp[0][1] = 1
MOD = 998244353

for i in range(0, N - 1):
    for j in range(2):
        for k in range(2):
            if AB[i][j] != AB[i + 1][k]:
                dp[i + 1][k] += dp[i][j]
                dp[i + 1][k] %= MOD

print(sum(dp[-1]) % MOD)
