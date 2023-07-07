N, M = map(int, input().split())
A = list(map(int, input().split()))

lst = A[2:]
lst.sort()

ans = 10 ** 18
print(N-M-1)
for i in range(N-M-1):
    temp = max(A[0] - lst[i], 0) + max(lst[i+M-1] - A[1], 0)
    ans = min(ans, temp)
    print(temp,ans,lst[i],lst[i+M-1])

print(ans)
