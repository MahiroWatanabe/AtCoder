N = int(input())
A = list(map(int,input().split()))
ans = 0

while all(A[i]%2 == 0 for i in range(N)):
    A = [A[i]//2 for i in range(N)]
    ans += 1

print(ans)