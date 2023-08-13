N,M = map(int, input().split())
S = list(input())
C = list(map(int,input().split()))
ps = [[] for _ in range(M)]
for i in range(N):
    ps[C[i]-1].append(i)

ans = S[:]

for i in range(M):
    l = len(ps[i])
    for j in range(l):
        ans[ps[i][(j+1)%l]] = S[ps[i][j]]

print("".join(ans))