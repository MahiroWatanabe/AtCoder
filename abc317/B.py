N = int(input())
A = sorted(list(map(int,input().split())))
D = set(A)

for i in range(1,A[-1]+1):
    if A[0] <= i <= A[-1] and i not in D:
        print(i)
        exit()