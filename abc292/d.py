class unionfind:
    def __init__(self,n):
        self.n = n
        self.par = [-1]*(n+1)
        self.size = [1]*(n+1)
    
    def root(self,x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unit(self,u,v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
    
    def same(self,u,v):
        return self.root(u) == self.root(v)
    
N,M = map(int, input().split())
into_num = [0]*N
R = [[0,set()] for _ in range(N)]

uf = unionfind(N)
UV = []

if M == 0:
    print("No")
    exit()
    
for _ in range(M):
    u,v = map(int, input().split())
    u,v = u-1,v-1
    UV.append([u,v])
    into_num[u] += 1
    into_num[v] += 1
    uf.unit(u,v)

for i in range(len(UV)):
    u,v = UV[i]
    G = uf.root(u)
    if not u in R[G][1]:
        R[G][0] += into_num[u]
        R[G][1].add(u)
    
    if not v in R[G][1]:
        R[G][0] += into_num[v]
        R[G][1].add(v)

for i in range(N):
    if R[i][0]//2 != len(R[i][1]):
        print("No")
        exit()
print("Yes")