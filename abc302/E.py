N,Q = map(int, input().split())
A = [set() for _ in range(N)]
ans = N

for _ in range(Q):
    value,*_a = map(int, input().split())
    if value == 1:
        u,v = _a
        u,v = u-1,v-1
        if len(A[u]) == 0:
            ans -= 1
        if len(A[v]) == 0:
            ans -= 1
        A[u].add(v)
        A[v].add(u)   
    else:
        v = _a[0]
        v -= 1
        if len(A[v]) != 0:
            for to in A[v]:
                A[to].discard(v)
                if len(A[to]) == 0:
                    ans += 1
            A[v].clear()
            ans += 1
    print(ans)