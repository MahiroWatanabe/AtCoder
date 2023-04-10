S = input()
flag = False
flag2 = False

for i in range(8):
    for j in range(8):
        if S[i] == "B" and S[j] == "B" and (i%2 != j%2):
            flag = True

K = S.index("K")

R_list = [i for i in range(8) if S[i]=="R"]

if R_list[0] < K < R_list[1]:
    flag2 = True

print("Yes" if flag and flag2 else "No")