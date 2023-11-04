# 二部グラフ判定
def dfs(c, x):
    global bipartite
    X[c] = x
    for d in g[c]:
        if X[d] == -1:
            dfs(d, 1 - x)
        elif X[d] == X[c]:
            bipartite = False


N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
g = [[] for _ in range(N)]
X = [-1] * N
bipartite = True

for i in range(M):
    A[i] -= 1
    B[i] -= 1
    g[A[i]].append(B[i])
    g[B[i]].append(A[i])

for i in range(N):
    if X[i] == -1:
        dfs(i, 0)

print("Yes" if bipartite else "No")
