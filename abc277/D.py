N,M = map(int, input().split())
A = sorted(list(map(int,input().split())))
G = [[A[0]]]

for i in range(1,N):
    if G[-1][-1] == A[i] or G[-1][-1]+1 == A[i]:
        G[-1].append(A[i])
    else:
        G.append([A[i]])

if 2 <= len(G) and G[0][0] == 0 and G[-1][-1]+1 == M:
    k = G[0]+G[-1]
    G.pop(0)
    G.pop()
    G.append(k)

Asum = sum(A)
ans = 10**15

for g in G:
    ans = min(ans,Asum-sum(g))

print(ans)