def do(bit):
    current_D = set()
    for i in range(M):
        if (bit >> i) & 1:
            for j in range(len(D[i])):
                current_D.add(D[i][j])
    for i in range(N):
        if i+1 not in current_D:
            return False
        
    return True

N,M = map(int, input().split())
D = []
for _ in range(M):
    C = int(input())
    A = list(map(int,input().split()))
    D.append(A)
ans = 0

for bit in range(2**M):
    if do(bit):
        ans += 1

print(ans)