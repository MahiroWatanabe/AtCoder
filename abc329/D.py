# 変化する値を考えることが大事
# 操作を行った時に変わるのは、投票が増えた人と今までで一番の人だけ

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

    print(index + 1)
