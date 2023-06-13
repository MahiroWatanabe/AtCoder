N = int(input())
S = input()
a,b = 0,0

for i in S:
    if i == "T":
        a += 1
    else:
        b += 1

if a < b:
    print("A")
elif a > b:
    print("T")
else:
    v = S[::-1][0]
    if v == "T":
        print("A")
    else:
        print("T")