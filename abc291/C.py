N = int(input())
S = input()
D = set()
D.add((0, 0))
x, y = 0, 0

for i in range(N):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    else:
        y -= 1

    if (x, y) in D:
        print("Yes")
        exit()
    else:
        D.add((x, y))
print("No")
