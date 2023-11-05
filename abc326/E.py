# 逆元の求め方 x**(p-2)
# pow(N,MOD-2,MOD)でできる
MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

invN = pow(N, MOD - 2, MOD)

dp = [0] * (N + 1)
s = 0
for i in range(N, 0, -1):
    dp[i] = A[i] + s * invN
    dp[i] %= MOD
    s += dp[i]
    s %= MOD

print((s * invN) % MOD)
