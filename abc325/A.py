N = input()

for i in range(len(N)-1):
    if not (N[i] > N[i+1]):
        print("No")
        exit()

print("Yes")