N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
current = []
for i in range(N):
    tmp = 0
    for j in range(M):
        if S[i][j] == "o":
            tmp += A[j]
    current.append(tmp + i + 1)

M_A = max(current)

for i in range(N):
    change_A = []
    for j in range(M):
        if S[i][j] == "x":
            change_A.append(A[j])
    change_A.sort(reverse=True)
    ans = 0
    while current[i] < M_A:
        current[i] += change_A[ans]
        ans += 1
    print(ans)
