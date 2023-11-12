# シンプルな累積和
N, Q = map(int, input().split())
S = input()
D = [0]
for i in range(N - 1):
    if S[i] == S[i + 1]:
        D.append(D[-1] + 1)
    else:
        D.append(D[-1])

for _ in range(Q):
    L, R = map(int, input().split())
    print(D[R - 1] - D[L - 1])
