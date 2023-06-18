L,N1,N2 = map(int, input().split())

events = []
t = 0
for i in range(N1):
    v,l = map(int, input().split())
    events.append([t,[0,v]])
    t += l
t = 0
for i in range(N2):
    v,l = map(int, input().split())
    events.append([t,[1,v]])
    t += l
    
events.sort()
events.append([L,[0,0]])
val = [0,0]
pt = 0
ans = 0

for t,p in events:
    if val[0] == val[1]:
        ans += t-pt
    i,v = p
    val[i] = v
    pt = t

print(ans)