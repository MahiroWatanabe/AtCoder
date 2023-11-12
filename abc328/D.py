# スタック　間の文字列を削除していく
S = input()
ans = []
for i in range(len(S)):
    ans.append(S[i])
    if len(ans) >= 3:
        a, b, c = ans.pop(), ans.pop(), ans.pop()
        if c + b + a != "ABC":
            ans.append(c)
            ans.append(b)
            ans.append(a)
print("".join(ans))
