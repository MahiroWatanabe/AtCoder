# 1増やして1減らすので、数列の合計が変わらない
# 数列に加算減算することで、平均に近づけていき、余りの数を数列に分散して加算する

N = int(input())
A = list(map(int, input().split()))
tmp = sum(A) // N
rem = sum(A) % N
B = [tmp for _ in range(N)]

for i in range(rem):
    B[i] += 1

A.sort()
B.sort()

ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])

print(ans // 2)
