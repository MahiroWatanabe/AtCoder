MOD = 998244353

def count_valid_parentheses(S):
    n = len(S)
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(n+1):
            if S[i-1] == '(' or S[i-1] == '?':
                if j-1 >= 0:
                    dp[i][j] += dp[i-1][j-1]
            if S[i-1] == ')' or S[i-1] == '?':
                if j < n:
                    dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD

    
    return dp[n][0]

S = input()
result = count_valid_parentheses(S)

print(result)
