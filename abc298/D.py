Q = int(input())
S = 1
MOD = 998244353
for _ in range(Q):
    x,*_a = map(int, input().split())
    if x == 1:
        v = _a[0]
        S = S * 10 + v
    elif x == 2:
        S = S % (10**(len(str(S))-1))
        S %= MOD
    else:
        S %= MOD
        print(S)
    print("A",str(S))