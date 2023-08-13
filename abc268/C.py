N = int(input())
P = list(map(int,input().split()))
ans = [0 for _ in range(N)]

for i in range(N):
    temp = ((P[i]-1)-i)%N
    ans[temp%N] += 1
    ans[(temp+1)%N] += 1
    ans[(temp+2)%N] += 1

print(max(ans))