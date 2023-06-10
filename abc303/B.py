N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
D = set()

for i in range(M):
    for j in range(N-1):
        a,b = A[i][j],A[i][j+1]
        D.add((min(a,b),max(a,b)))

print((N*(N-1)//2)-len(D))