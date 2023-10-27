# 二項係数
MOD = 998244353

def COMinit():
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX

    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i
        inv[i] = MOD - inv[MOD%i] * (MOD // i)
        finv[i] = finv[i - 1] * inv[i]

    return fac, finv

def COM(n, k, fac, finv):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * finv[k] * finv[n - k]

MAX = 510000
fac, finv = COMinit()

result = COM(100000, 50000, fac, finv)
print(result)
