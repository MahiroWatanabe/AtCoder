from heapq import heappop, heappush

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(t) - 1 for t in input().split()]
    G[a].append(b)
    G[b].append(a)

que = []  # 優先度付きキュー,  (-体力,pos)を格納する
for _ in range(K):
    p, h = map(int, input().split())
    heappush(que, (-h, p - 1)) 

seen = set()

while que:
    mh, pos = heappop(que)
    h = -mh
    if pos in seen:
        continue
    seen.add(pos)
    if h == 0:
        continue
    for nv in G[pos]:
        if nv in seen:
            continue
        heappush(que, (mh + 1, nv))

ans_list = list(seen)
ans_list.sort()
print(len(ans_list))
print(*[a + 1 for a in ans_list])

