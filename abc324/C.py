# 計算量わかりにくい　編集距離
N, T = input().split()
N = int(N)
ans = []
for i in range(N):
    S = input()

    if len(T) == len(S):
        if T == S:
            ans.append(i + 1)
        else:
            tmp = 0
            for j in range(len(T)):
                if T[j] != S[j]:
                    tmp += 1
            if tmp == 1:
                ans.append(i + 1)

    elif len(T) + 1 == len(S):
        if S[:-1] == T:
            ans.append(i + 1)
            continue

        for j in range(len(T)):
            if S[j] != T[j]:
                if S[j + 1 :] == T[j:]:
                    ans.append(i + 1)
                break

    elif len(T) == len(S) + 1:
        if T[:-1] == S:
            ans.append(i + 1)
            continue

        for j in range(len(S)):
            if T[j] != S[j]:
                if T[j + 1 :] == S[j:]:
                    ans.append(i + 1)
                break

print(len(ans))
ans.sort()
print(*ans)
