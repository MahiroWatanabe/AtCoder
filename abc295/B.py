R,C = map(int, input().split())
B = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        for k in range(R):
            for l in range(C):
                if B[i][j] == "#" and B[k][l] != "#" and B[k][l] != ".":
                    if abs(i-k)+abs(j-l) <= int(B[k][l]):
                        B[i][j] = "."

for i in B:
    ans = ""
    for j in i:
        if j != "." and j != "#":
            ans += "."
        else:
            ans += j
    print(ans)