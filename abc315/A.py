S = input()
ans = ""
for i in S:
    if i in "aeiou":
        continue
    else:
        ans += i

print(ans)