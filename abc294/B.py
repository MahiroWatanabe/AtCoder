# 行列 A を読み込む
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 文字列 S を生成する
S = []
for i in range(H):
    s = ""
    for j in range(W):
        if A[i][j] == 0:
            s += "."
        else:
            s += chr(A[i][j] + 64)
    S.append(s)

# 文字列 S を出力する
for s in S:
    print(s)
