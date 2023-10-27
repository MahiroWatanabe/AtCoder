# 入力の受け取り
N=int(input())
A=list(map(int, input().split()))

# defaultdictをインポート
from collections import defaultdict
# 初期値は空のリスト
indx=defaultdict(list)

# i=0~(N-1)
for i in range(N):
    # 各要素のインデックス番号を記録
    indx[A[i]].append(i)

# 「X」を両端(Ai,Ak)としたときの組み合わせ数を確認する関数
def indxCount(X):
    # リストの長さ
    n=len(X)
    # 組み合わせ数
    count=0

    # i=0~(n-1)
    for i in range(n):
        # +X[i]がi個
        count+=X[i]*i
        # -X[i]が(n-i-1)個
        count-=X[i]*(n-i-1)
    
    # i=0~(n-1)
    for i in range(n):
        # -iが(n-i-1)個
        count-=i*(n-i-1)

    # -1がnC2=n*(n-1)//2個
    count-=n*(n-1)//2

    # 値を返す
    return count

# 答え
ans=0

# Xlist：indxの値を順に代入
for Xlist in indx.values():
    # 答えにプラス
    ans+=indxCount(Xlist)

# 答えの出力
print(ans)
