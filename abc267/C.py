N,M = map(int, input().split())
A = list(map(int,input().split()))
S,T = 0,0

for i in range(M):
    S += A[i]*(i+1)
for i in range(M):
    T += A[i]

ans = S
for i in range(N-M):
    ns = S-T+A[i+M]*M
    nt = T-A[i]+A[i+M]
    S = ns
    T = nt
    ans = max(ans,S)

print(ans)