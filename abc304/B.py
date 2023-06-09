N = int(input())

if N <= 10**3-1:
    print(N)
elif 10**3 <= N <= 10**4-1:
    print(str(N)[:-1]+"0")
elif 10**4 <= N <= 10**5-1:
    print(str(N)[:-2]+"00")
elif 10**5 <= N <= 10**6-1:
    print(str(N)[:-3]+"000")
elif 10**6 <= N <= 10**7-1:
    print(str(N)[:-4]+"0000")
elif 10**7 <= N <= 10**8-1:
    print(str(N)[:-5]+"00000")
elif 10**8 <= N <= 10**9-1:
    print(str(N)[:-6]+"000000")