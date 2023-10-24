# dp問題　すでに議席を書くときしている時の遷移を含む必要ある
N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]
Taka,Aoki = 0,0
S_Z = 0
for i,j,k in XYZ:
    if i < j:
        Aoki += k
    else:
        Taka += k
    S_Z += k
INF = 10**20  
if Aoki < Taka:
    print(0)
else:
    tar = ((Taka+Aoki)//2+1)-Taka
    dp = [[INF for _ in range(S_Z+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(S_Z+1):
            if dp[i][j] != INF:
                if XYZ[i][0] < XYZ[i][1]:
                    people = (XYZ[i][0]+XYZ[i][1])//2+1-XYZ[i][0]
                else:
                    # すでに議席を書くときしている時は移動0で議席を獲得できる
                    people = 0
                dp[i+1][j+XYZ[i][2]] = min(dp[i+1][j+XYZ[i][2]] ,dp[i][j] + people)
                dp[i+1][j] = min(dp[i+1][j],dp[i][j])

    ans = INF
    for i in range(S_Z//2+1,S_Z+1):
        ans = min(ans,dp[-1][i])
    print(ans)