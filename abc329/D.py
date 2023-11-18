N, M = map(int, input().split())
A = list(map(int, input().split()))
D = [0 for _ in range(N)]
current = 0
index = 0

for i in range(M):
    D[A[i] - 1] += 1
    if current < D[A[i] - 1]:
        current = D[A[i] - 1]
        index = A[i] - 1
    if current == D[A[i] - 1]:
        index = min(index, A[i] - 1)

    # print(D)
    print(index + 1)
