# 後ろの要素に依存して考える必要があるので、配列を逆にして後ろから見ていく
N,M = map(int, input().split())
A = set(list(map(int,input().split())))
cnt = 1
ans = []

for i in range(N,0,-1):
    if i in A:
        ans.append(0)
        cnt = 1
    else:
        ans.append(cnt)
        cnt += 1

print(*ans[::-1])