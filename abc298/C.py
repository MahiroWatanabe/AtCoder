N = int(input())
Q = int(input())
M = 200001
box = [[] for _ in range(N+1)]
card = [set() for _ in range(M)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, j = q[1:]
        box[j].append(i)
        card[i].add(j)
    elif q[0] == 2:
        print(*sorted(box[q[1]]))
    else:
        print(*sorted(card[q[1]]))
