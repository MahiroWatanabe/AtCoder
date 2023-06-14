N = int(input())
L,R = 1,N

while R-L > 1:
    mid = (L+R)//2
    print("?",mid)
    v = int(input())
    if v == 0:
        L = mid
    else:
        R = mid
        
print("!",str(L))