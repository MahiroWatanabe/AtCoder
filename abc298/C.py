MOD = 998244353
Q = int(input())
S = [1]  # スタックに最初は1を入れておく
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        S.append(query[1])
    elif query[0] == 2:
        S.pop(0)
    else:
        # スタックの要素を10進数表記の数と見なして計算する
        n = len(S)
        res = 0
        for i in range(n):
            res = (res * 10 + S[i]) % MOD
        print(res)
