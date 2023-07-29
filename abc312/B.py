def f(x,y):
    for k in range(9):
        for l in range(9):
            i = x+k
            j = y+l
            if k <= 2 and l <= 2 and S[i][j] != "#":
                return False
            if 6 <= k and 6 <= l and S[i][j] != "#":
                return False
            if ((k == 3 and l <= 3 and S[i][j] != ".") or
                    (k <= 3 and l == 3 and S[i][j] != ".") or
                    (k == 5 and 5 <= l and S[i][j] != ".") or
                    (5 <= k and l == 5 and S[i][j] != ".")):
                return False
            
    return True

N,M = map(int, input().split())
S = [input() for _ in range(N)]
ans = []

for i in range(N):
    if i+9 <= N:
        for j in range(M):
            if j+9 <= M:
                if f(i,j):
                    ans.append([i+1,j+1])

for i in ans:
    print(*i)