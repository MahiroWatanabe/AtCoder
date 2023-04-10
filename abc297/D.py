A,B = map(int, input().split())
ans = 0
A,B = max(A,B),min(A,B)
while B != 0:
    ans += A//B
    A %= B
    A,B = max(A,B),min(A,B)

print(ans-1)