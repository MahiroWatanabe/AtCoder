N = int(input())
for i in range(N, 10**6 + 1):
    v = str(i)
    if int(v[0]) * int(v[1]) == int(v[2]):
        print(v)
        exit()
