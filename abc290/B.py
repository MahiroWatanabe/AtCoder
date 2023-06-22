N = int(input())
X = sorted(list(map(int,input().split())))
ans = 0

for i in range(N,len(X)-N):
    ans += X[i]
    
print(ans/(3*N))