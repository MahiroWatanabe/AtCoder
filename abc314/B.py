N = int(input())
ans = []
Q = []
W = []
for _ in range(N):
    K = int(input())
    B = set(list(map(int,input().split())))
    Q.append(K)
    W.append(B)
X = int(input())

ans = []
min_now = 10**18

for i in range(N):
    if X in W[i]:
        min_now = min(min_now,len(list(W[i])))
        
cnt = 0

for i in range(N):
    if X in W[i] and len(list(W[i])) == min_now:
        cnt += 1
        ans.append(i+1)

if cnt == 0:
    print(0)
    print()
else:
    print(cnt)
    print(*ans)