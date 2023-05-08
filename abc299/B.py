N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

flag = False

ans = 0
current_max = 0
for i in range(N):
    if C[i] == T:
        flag = True
        if current_max < R[i]:
            current_max = R[i]
            ans = i + 1

if flag:
    print(ans)
    exit()

ans = 1
current_max = R[0]
for i in range(1, N):
    if C[i] == C[0]:
        if current_max < R[i]:
            current_max = R[i]
            ans = i + 1

print(ans)
