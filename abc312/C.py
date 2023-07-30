N,M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
L,R = 0,10**9

while R-L > 1:
    mid = (L+R)//2
    na = 0
    nb = 0
    for i in range(N):
        if A[i] <= mid:
            na += 1
    for i in range(M):
        if B[i] >= mid:
            nb += 1
    if na >= nb:
        R = mid
    else:
        L = mid

print(R)