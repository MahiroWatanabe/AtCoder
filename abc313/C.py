N = int(input())
A = list(map(int,input().split()))
temp = sum(A)//N
ans = 0

for i in A:
    ans += min(abs(temp-i),abs(temp+1-i))

print(ans//2 if ans%2 == 0 else ans//2+1)