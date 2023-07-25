N = int(input())
A = [int(i)-1 for i in input().split()]
S = [0]
D = set([0])
v = 0

while True:
    nv = A[v]
    
    if nv in D:
        idx = S.index(nv)
        ans = S[idx:]
        print(len(ans))
        print(*[a+1 for a in ans])
        break
    else:
        D.add(nv)
        S.append(nv)
        v = nv