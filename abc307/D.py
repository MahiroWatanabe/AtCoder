N = int(input())
S = input()
cnt = 0
D = []

for i in range(N):
    if S[i] == "(":
        cnt += 1
        D.append(S[i])
    elif S[i] == ")":
        if cnt > 0:
            cnt -= 1
            while True:
                if D.pop() == "(":
                    break
        else:
            D.append(S[i])
    else:
        D.append(S[i])

print(*D,sep="")