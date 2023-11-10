def judge(v):
    if 0 <= v <= 100:
        return True
    else:
        False


C = [list(map(int, input().split())) for _ in range(3)]

for a1 in range(101):
    b1 = C[0][0] - a1
    b2 = C[0][1] - a1
    b3 = C[0][2] - a1

    if judge(b1) and judge(b2) and judge(b3):
        a2 = C[1][0] - b1
        a3 = C[2][0] - b1

        if judge(a2) and judge(a3):
            if (
                C[0][0] == a1 + b1
                and C[0][1] == a1 + b2
                and C[0][2] == a1 + b3
                and C[1][0] == a2 + b1
                and C[1][1] == a2 + b2
                and C[1][2] == a2 + b3
                and C[2][0] == a3 + b1
                and C[2][1] == a3 + b2
                and C[2][2] == a3 + b3
            ):
                print("Yes")
                exit()

print("No")
