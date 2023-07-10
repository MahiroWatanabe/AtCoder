N,K = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(N)])
S = sum(j for i,j in AB)
if S <= K:
    print(1)
    exit()
for i in range(N):
    S -= AB[i][1]
    if S <= K:
        print(AB[i][0]+1)
        exit()