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
g = [[] for _ in range(N)]
uf = unionfind(N)
    
for _ in range(M):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    if uf.same(u,v):
        print("No")
        exit()
    uf.unit(u,v)
    g[u].append(v)
    g[v].append(u)
if M == 0:
    print("No")
    exit()

if N-1 != M:
    print("No")
    exit()
for i in g:
    if len(i) >= 3:
        print("No")
        exit()

print("Yes")