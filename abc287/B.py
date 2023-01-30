N,M = map(int, input().split())
S = [input()[3:] for _ in range(N)]
T = [input() for _ in range(M)]
cnt = 0

for i in S:
    for j in T:
        if i == j:
            cnt += 1
            break

print(cnt)