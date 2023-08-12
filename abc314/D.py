N = int(input())
S = list(input())
Q = int(input())

operations = []
for _ in range(Q):
    t, x, c = input().split()
    t = int(t)
    x = int(x) if t == 1 else 0
    operations.append((t, x, c))
a,b = 0,0

for i in range(Q):
    if operations[i][0] == 2:
        a = i
    elif operations[i][0] == 3:
        b = i

for i in range(max(a,b)+1):
    t, x, c = operations[i]
    if t == 1:
        S[x - 1] = c
        
S = "".join(S)

if a < b:
    S = S.upper()
elif a > b:
    S = S.lower()
    
S = list(S)

for i in range(max(a,b)+1,Q):
    t, x, c = operations[i]
    if t == 1:
        S[x-1] = c
    
print("".join(S))