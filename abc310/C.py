N = int(input())
D = set()

for _ in range(N):
    S = input()
    if S not in D and S[::-1] not in D:
        D.add(S)

print(len(D))