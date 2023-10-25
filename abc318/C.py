N,D,P = map(int, input().split())
F = sorted(list(map(int,input().split())))
ans = 0

while True:
    if len(F) < D:
        q = sum(F)
        if P < q:
            ans += P
        else:
            ans += q
        print(ans)
        exit()
    tmp = 0
    for i in range(D):
        tmp += F.pop()
        
    if P < tmp:
        ans += P
    else:
        ans += tmp