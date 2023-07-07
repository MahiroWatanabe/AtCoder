N,M = map(int, input().split())
A = list(map(int,input().split()))
l,r = A[0],A[1]
D = A[2:]
ans = 0
R = []
for i in range(len(D)):
    if not l <= D[i] <= r:
        R.append(min(abs(D[i]-l),abs(D[i]-r)))
    else:
        M -= 1
        
print(M)
R.sort()
print(R)
print(sum(R[:3]))