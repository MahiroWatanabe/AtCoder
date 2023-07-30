N,M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
L,R = 0,10**10

while R-L > 1:
    mid = (L+R)//2
    a,b = 0,0
    
    for i in range(N):
        if A[i] <= mid:
            a += 1
    for i in range(M):
        if mid <= B[i]:
            b += 1
    if a < b:
        L = mid
    else:
        R = mid

print(R)