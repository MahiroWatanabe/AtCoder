N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = set(list(map(int,input().split())))
X = int(input())
dp = [False for _ in range(X+1)]
dp[0] = True

for i in range(X):
    if dp[i] != False:
        for k in range(N):
            v = i+A[k]
            if v < X+1 and v not in B:
                dp[v] = True

print("Yes" if dp[-1] else "No")