def f(W):
    current = 0
    cnt = 1
    
    for i in range(N):
        if W < current + L[i]:
            cnt += 1
            current = 0
        if current + L[i] <= W:
            current += L[i]+1
            
    return cnt <= M

N,M = map(int, input().split())
L = list(map(int,input().split()))
left,right = max(L)-1,10**20

while abs(right-left) > 1:
    mid = (left+right)//2
    
    if f(mid):
        right = mid
    else:
        left = mid

print(right)